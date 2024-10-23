import logging, os
import pickle, dill
from datetime import datetime
import time

from contextlib import redirect_stdout

from config import LOGS_BUCKET
from base import BaseTask

import subprocess

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


class PythonTask(BaseTask):
    def __init__(self, callable, show_return_value_in_logs = False, **kw_args):
        super().__init__()
        self.callable = callable
        self.kw_args = kw_args
        self.show_return_value_in_logs = show_return_value_in_logs
        # initialize task

    def run(self):
        self.log_platform_info()
        self.redis_logger.info(f"Started running {self.callable}, task_id: {self.get_task_id()}")
        self.redis_logger.info(f"show_return_value_in_logs: {self.show_return_value_in_logs}")
        with redirect_stdout(StreamToLogger(self.redis_logger, logging.INFO)):
            try:
                if self.show_return_value_in_logs:
                    self.redis_logger.info(f"Return value: {self.callable(**self.kw_args)}")
                else:
                    self.callable(**self.kw_args)
                self.redis_logger.info(f"Return code: 0")
            except Exception as e:
                self.redis_logger.error(f"Exception in {self.callable}: {str(e)}")
                self.redis_logger.info(f"Return code: -1")
            print(f"Saving logs to gs://{LOGS_BUCKET}/{self.redis_logger_key}")
        self.close_and_save_logs()


class PythonVirtualEnvTask(BaseTask):
    def __init__(self, callable, requirements, show_return_value_in_logs = False, requirements_file=None, python_version=None, op_args =[], op_kwargs={}):
        super().__init__()
        self.callable = callable
        self.requirements_file = requirements_file
        # self.requirements = ", ".join([r.strip() for r in requirements]) if isinstance(requirements, list) == True else requirements.strip()
        self.requirements = [r.strip() for r in requirements] if isinstance(requirements, list) == True else requirements.strip()
        self.op_args = op_args
        self.op_kwargs = op_kwargs
        self.env_name = f"venv-{self.get_task_id()}"
        self.python_version = python_version
        self.venv_dir = f"/tmp/{self.env_name}"
        self.show_return_value_in_logs = show_return_value_in_logs


    def create_python_venv(self):
        try:
            self.redis_logger.info(f"Creating virtual environment: {self.venv_dir}")
            command = ["python", "-m", "venv", self.venv_dir]
            result = subprocess.run(command, check=True, capture_output=True)
            print("Standard output:", result.stdout.decode('utf-8'))
            print("Standard error:", result.stderr.decode('utf-8'))
            
            self.redis_logger.info(f"Installing packages: {self.requirements}")
            command = [f"{self.venv_dir}/bin/pip", "install"]
            for package in self.requirements:
                command.append(package)
            result = subprocess.run(command, check=True, capture_output=True)
            print("Standard output:", result.stdout.decode('utf-8'))
            print("Standard error:", result.stderr.decode('utf-8'))
        except Exception as e:
            self.redis_logger.error(f"An exception occurred in create_python_venv: {str(e)}")
            raise e


    def call_deserialized(self):
        # Deserialize the callable from the file: deserialized_callable
        self.redis_logger.info(f"Running callable: {self.venv_dir}/serialized_callable.pkl")
        command = [f"{self.venv_dir}/bin/python", "pyvenv-exec-callable.py", f"{self.venv_dir}"]
        working_directory = os.path.dirname(__file__)
        result = subprocess.run(command, check=True, cwd=working_directory, capture_output=True)
        print("Standard output:", result.stdout.decode('utf-8'))
        print("Standard error:", result.stderr.decode('utf-8'))
        return result
        
        
    def serialize_callable(self):
        # Serialize the callable to a file: serialized_callable.pkl
        with open(f"{self.venv_dir}/serialized_callable.pkl", 'wb') as f:
            dill.dump((self.callable, self.show_return_value_in_logs, self.op_args, self.op_kwargs), f)


    # SerDe - Callable 
    """
    # Serialize
    import dill
    dill.settings["recurse"] = True
    with open(f"{self.venv_dir}/serialized_callable.pkl", 'wb') as f:
        dill.dump((self.callable, self.op_args, self.op_kwargs), f)
    
    # Deserialize
    import dill
    with open(f"{venv_dir}/serialized_callable.pkl", 'rb') as f:
        deserialized_callable, op_args, op_kwargs = dill.load(f)
    result = deserialized_callable(*op_args, **op_kwargs)
    """
    
    def run(self):
        self.log_platform_info()
        self.redis_logger.info(f"Started running {self.callable}, task_id: {self.get_task_id()}")
        self.redis_logger.info(f"show_return_value_in_logs: {self.show_return_value_in_logs}")

        # self.create_python_venv()
        # self.serialize_callable()
        # result = self.call_deserialized()
        
        with redirect_stdout(StreamToLogger(self.redis_logger, logging.INFO)):
            try:
                self.create_python_venv()
                self.serialize_callable()
                result = self.call_deserialized()
                print(result)
                self.redis_logger.info(f"Return code: 0")
            except Exception as e:
                self.redis_logger.error(f"Exception in {self.callable}: {str(e)}")
                self.redis_logger.info(f"Return code: -1")
            print(f"Saving logs to gs://{LOGS_BUCKET}/{self.redis_logger_key}")
        self.close_and_save_logs()


if __name__ == "__main__":
    # Functions for testing 
    import numpy as np
    
    def say_hello():
        print("Hello, world!")


    def say_hi():
        print(f"__file__: {__file__}")
        print(os.path.abspath(__file__))
        print(os.path.dirname(__file__))
        print(os.path.basename(__file__))
        print(os.path.basename(__file__).rstrip(".py"))
        say_hi_for_name("abc")


    def get_numpy_version():
        print("abc")
        print(f"printing np.__version__: {np.__version__}") 
        return (np.__version__)


    def print_numpy_with_name(name):
        print(f"Printing np.__version__: {np.__version__}, name: {name}") 
        return f"np.__version__:{np.__version__}, name: {name}"


    def say_hi_for_name(name = "world"):
        return print(f"Hello {name}!")


    def say_hi():
        print("Hello, world!")


    def say_hi_for_name(name):
        print(f"Print Name: {name}!")
        return f"Name: {name}!"


    def say_hi_with_time():
        print(f"Hello, India! It's {datetime.now()}\n")
        print(f"Hello, World! It's {datetime.now()}\n")
        print(f"Hello, Earth! It's {datetime.now()}\n")
        print(f"Hello, Universe! It's {datetime.now()}\n")
        return "Hello, Hello!"


    def long_task_with_logs(n:int):
        for i in range(n):
            print(f"Long task running: {i}")
            time.sleep(2)
        return "Long task done!"


    def say_hi_with_time():
        print(f"Hello, India! It's {datetime.now()}\n")
        print(f"Hello, World! It's {datetime.now()}\n")
        print(f"Hello, Earth! It's {datetime.now()}\n")
        print(f"Hello, Universe! It's {datetime.now()}\n")
        return "Hello, Hello!"


    def get_numpy_version():
        print(np.__version__) 
    
    # say_hi()
    # say_hi_with_time()
    # print(get_numpy_version())
    
    # pt = PythonTask(callable = say_hi)
    # pt.run()
    # pt = PythonTask(callable = say_hi_for_name, name = "Docket", show_return_value_in_logs = True)
    # pt.run()
    
    # PythonTask(callable = say_hi_with_time, show_return_value_in_logs = True).run()
    # PythonTask(callable = long_task_with_logs, show_return_value_in_logs = True, n=2).run()
    # # PythonTask(callable = get_numpy_version, kw_args = {}).run()    
    
    # x = PythonTask(callable = get_numpy_version, ).run()
    # print(x)
    
    # x = PythonVirtualEnvTask(callable=say_hello, requirements=["numpy", "pandas", "redis", "google-cloud-storage", "dill"]).run()
    # print(x)
    # y = PythonVirtualEnvTask(
    #     callable=print_numpy_with_name, 
    #     show_return_value_in_logs=True, 
    #     requirements=["numpy", "pandas", "redis", "google-cloud-storage", "dill"], 
    #     op_kwargs={"name": "xyz"}
    #     ).run()
    # print(y)
    