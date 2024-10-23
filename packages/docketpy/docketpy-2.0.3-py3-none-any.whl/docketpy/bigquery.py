"""
    input - 
        * sql_string or sql_file [only one of them is required]
        * project_id
        - service_account_key {optional}
        - gcp_connection_id [optional]
    }
"""

from google.cloud import bigquery
from google.oauth2 import service_account
from concurrent.futures import ThreadPoolExecutor, TimeoutError


# # Replace with your own credentials file
# credentials = service_account.Credentials.from_service_account_file('path_to_your_service_account_key.json')

# # Set your project and dataset
# project_id = 'your_project_id'
# dataset_id = 'your_dataset_id'
# table_id = 'users'

# # Initialize the BigQuery client
# client = bigquery.Client(credentials=credentials, project=project_id)

# # Define the table schema
# schema = [
#     bigquery.SchemaField('user_id', 'INT64', mode='REQUIRED'),
#     bigquery.SchemaField('name', 'STRING', mode='REQUIRED'),
#     bigquery.SchemaField('email', 'STRING', mode='REQUIRED'),
#     bigquery.SchemaField('signup_date', 'DATE', mode='REQUIRED'),
# ]

# # Create the table
# table_ref = client.dataset(dataset_id).table(table_id)
# table = bigquery.Table(table_ref, schema=schema)
# table = client.create_table(table)  # Make an API request.
# print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")

# # Insert random data into the table
# query = f"""
# INSERT INTO `{project_id}.{dataset_id}.{table_id}` (user_id, name, email, signup_date)
# SELECT 
#   CAST(ROW_NUMBER() OVER() AS INT64) AS user_id,
#   CONCAT('User_', CAST(FLOOR(RAND() * 1000000) AS STRING)) AS name,
#   CONCAT('user', CAST(FLOOR(RAND() * 1000000) AS STRING), '@example.com') AS email,
#   DATE_SUB(CURRENT_DATE(), INTERVAL CAST(FLOOR(RAND() * 365) AS INT64) DAY) AS signup_date
# FROM 
#   UNNEST(GENERATE_ARRAY(1, 10));
# """

# # Run the query
# query_job = client.query(query)
# query_job.result()  # Wait for the job to complete.
# print("Inserted random data into the table.")


import logging, os
import pickle, dill
from datetime import datetime
import time

from contextlib import redirect_stdout

from config import LOGS_BUCKET
from base import BaseTask
from exceptions import NotImplmentedInDocketError


dill.settings["recurse"] = True

class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, level):
       self.logger = logger
       self.level = level
       self.linebuf = ''
       self._in_write = False
    
    def write(self, message):
        # Avoid empty messages and recursion
        if not self._in_write and message.strip():  
            self._in_write = True
            try:
                self.logger.log(self.level, message.strip())
            finally:
                self._in_write = False

    def flush(self):
        pass


class BigQueryTask(BaseTask):
    def __init__(self, 
                 sql, 
                 service_account_key, 
                 project, 
                 show_return_value_in_logs = False, 
                 query_wait_timeout = 300, 
                 **kw_args):
        super().__init__()
        self.sql = sql
        self.project = project
        self.credentials = service_account.Credentials.from_service_account_file(service_account_key)
        self.bq_client = bigquery.Client(credentials=self.credentials, project=self.project)
        self.show_return_value_in_logs = show_return_value_in_logs
        self.query_wait_timeout = query_wait_timeout
        self.kw_args = kw_args

    def run(self):
        self.log_platform_info()
        self.redis_logger.info(f"Started running BigQuery SQL, task_id: {self.get_task_id()}")
        self.redis_logger.info(f"show_return_value_in_logs: {self.show_return_value_in_logs}")
        with redirect_stdout(StreamToLogger(self.redis_logger, logging.INFO)):
            try:
                if self.show_return_value_in_logs:
                    self.redis_logger.info(f"Return value: {self.execute_sql()}")
                else:
                    self.execute_sql()
                self.redis_logger.info(f"Return code: 0")
            except Exception as e:
                self.redis_logger.error(f"Exception in {self.execute_sql.__name__}: {str(e)}")
                self.redis_logger.info(f"Return code: -1")
            print(f"Saving logs to gs://{LOGS_BUCKET}/{self.redis_logger_key}")
        self.close_and_save_logs()

    def execute_sql(self):
        try:
            query_job = self.bq_client.query(self.sql)
            print(f"Submitted to BigQuery, Job ID: {query_job.job_id}, query_wait_timeout: {self.query_wait_timeout}")
            print("Query waiting for completion...")
            return query_job.result(timeout=self.query_wait_timeout)
        except TimeoutError:
            print('Query timed out')
            return None
        except Exception as e:
            print(f"An exception occurred while running the query: {str(e)}")
            return None


if __name__ == "__main__":
    # Test cases 
    sql = """
        CREATE TABLE  IF NOT EXISTS `wf-gcp-us-ae-bigdata-prod.data_services.users` (
        user_id INT64,
        name STRING,
        email STRING,
        birth_date DATE
        ); 
        INSERT INTO `wf-gcp-us-ae-bigdata-prod.data_services.users` (user_id, name, email, birth_date)
        SELECT 
        CAST(ROW_NUMBER() OVER() AS INT64) AS user_id,
        CONCAT('User_', split(GENERATE_UUID(), '-')[4]) AS name,
        CONCAT('user', split(GENERATE_UUID(), '-')[4], '@wayfair.com') AS email,
        DATE_SUB(CURRENT_DATE(), INTERVAL CAST(FLOOR(RAND() * 25000) AS INT64) DAY) AS birth_date
        FROM UNNEST(GENERATE_ARRAY(1, 1000))
        ;
    """ 
    
    bq = BigQueryTask(
        sql = sql, 
        project = "wf-gcp-us-ae-bigdata-prod", 
        service_account_key='/Users/st201n/wf-us-ae-svc-kronos.json',
        show_return_value_in_logs = True)
    bq.run()
    
    worst_sql = f"""
        WITH repetitive_cte AS (
        SELECT
            1 AS num
        FROM
            UNNEST(GENERATE_ARRAY(1, 10000)) AS num
        )
        SELECT
        COUNT(*)
        FROM
        repetitive_cte AS r1
        CROSS JOIN
        repetitive_cte AS r2
        CROSS JOIN
        `bigquery-public-data.samples.natality` AS n
        WHERE
        n.year > 1980
    """
    
    bq2 = BigQueryTask(
        sql = worst_sql, 
        project = "wf-gcp-us-ae-bigdata-prod", 
        service_account_key='/Users/st201n/wf-us-ae-svc-kronos.json',
        show_return_value_in_logs = True, 
        query_wait_timeout = 60)
    bq2.run()
    