import redis
from google.cloud import storage

def read_list_from_redis(redis_host, redis_port, redis_key, redis_db=0):
    """Reads a list from Redis."""
    client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    return client.lrange(redis_key, 0, -1)


def save_to_gcs(bucket_name, destination_blob_name, data_list):
    """Uploads a file to Google Cloud Storage."""
    # Initialize a GCS client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a new blob and upload the data
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string('\n'.join(data_list), content_type='text/plain')


def save_logs_to_bucket_from_redis(redis_host, redis_port, redis_key, bucket_name, destination_blob_name):
    # Read data from Redis
    raw_data_list = read_list_from_redis(redis_host, redis_port, redis_key)
    
    # Convert bytes to strings
    data_list = [item.decode('utf-8') for item in raw_data_list]

    # Save to GCS
    save_to_gcs(bucket_name, destination_blob_name, data_list)
    print(f"Data saved to GCS bucket gs://{bucket_name}/{destination_blob_name}")


def create_bucket(bucket_name, project_id=None):
    """Creates a GCS bucket if it doesn't exist.
    Args:
    bucket_name: The name of the bucket to create.
    project_id: The ID of the GCP project where the bucket will be created.
        If not specified, uses the default project from the Google Cloud credentials.

    Returns:
    The created or existing bucket object.
    """

    # Create a storage client
    client = storage.Client(project=project_id)

    # Check if the bucket already exists
    bucket = client.bucket(bucket_name)
    if bucket.exists():
        print(f"Bucket '{bucket_name}' already exists.")
        return bucket
    else:
        # Create the bucket
        bucket = client.create_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created.")
        return bucket
