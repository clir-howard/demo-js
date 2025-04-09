#!/usr/bin/env python3
import boto3

def call_aws_api():
    # 使用虚拟的 AWS Access Key 和 Secret Key
    aws_access_key = "YOUR_AK"
    aws_secret_key = "YOUR_SK"
    region = "us-west-2"

    # 创建一个 boto3 会话
    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )

    # 例如：调用 S3 API 列举所有 S3 桶
    s3 = session.client("s3")
    try:
        response = s3.list_buckets()
        buckets = response.get("Buckets", [])
        print("S3 Buckets:")
        for bucket in buckets:
            print(" -", bucket["Name"])
    except Exception as e:
        print("调用 AWS API 出现错误:", e)

if __name__ == "__main__":
    call_aws_api()
