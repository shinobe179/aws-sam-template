import json
import os

# import requests
import boto3
from botocore.exceptions import ClientError


def run(event, context):
    print('Function works.')
    print(json.dumps(get_secret(os.environ['SECRET_ARN'])))


def get_secret(arn):

    region_name = "ap-northeast-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=arn
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    print('secret: ', secret)

    return secret
