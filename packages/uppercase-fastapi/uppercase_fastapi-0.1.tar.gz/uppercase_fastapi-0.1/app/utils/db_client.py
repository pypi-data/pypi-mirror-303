import psycopg2
import json
import boto3
import logging
from fastapi import HTTPException
from app.utils.config import (
    HOST,
    DB,
    DB_ENV,
    SECRET_NAME,
)


class dbClient:
    @staticmethod
    def get_secret():
        """
        Function to return DB creds from secrets manager
        """
        try:
            secret = boto3.client(service_name='secretsmanager')
            secret_response = secret.get_secret_value(SecretId=SECRET_NAME)
            if json.loads(secret_response['SecretString']):
                return secret_response['SecretString']
            else:
                raise HTTPException(status_code=500, detail="No secret found")
        except Exception as e:
            logging.error('Could not retrieve DB creds from secrets manager')
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

   
