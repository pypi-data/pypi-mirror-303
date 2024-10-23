import os
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.environ.get('log_level', 'INFO')
HOST = os.environ.get('rds_host', '')
PORT = os.environ.get('rds_port', '5432')
DB = 'cds_' + os.environ.get('database_env', '')
DB_ENV = os.environ.get('database_env', '')
SECRET_NAME = os.environ.get('secret_name', '')
