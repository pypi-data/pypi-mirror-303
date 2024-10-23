import os 
LOGS_BUCKET = "st-temp-docket-logs-bucket"
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
# print(f"REDIS_HOST: {REDIS_HOST}")
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
# print(f"REDIS_PORT: {REDIS_PORT}")
