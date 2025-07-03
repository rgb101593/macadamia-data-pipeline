import boto3
from pyspark.sql import SparkSession
import os

def save_to_s3(df, bucket_name, key_prefix):
    """Save processed data to S3 (for cloud analytics)"""
    # Write as Parquet (optimized for analytics)
    temp_path = f"/tmp/{key_prefix}"
    df.write.parquet(temp_path, mode="overwrite")
    
    # Upload to S3
    s3 = boto3.client('s3')
    for root, _, files in os.walk(temp_path):
        for file in files:
            local_path = os.path.join(root, file)
            s3_key = f"{key_prefix}/{file}"
            s3.upload_file(local_path, bucket_name, s3_key)
    print(f"✅ Uploaded {df.count()} records to s3://{bucket_name}/{key_prefix}")