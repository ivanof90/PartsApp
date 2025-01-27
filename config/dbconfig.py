#Databse configuration information
import os

from dotenv import load_dotenv

load_dotenv()

pg_config = {
    'user' : os.environ.get('DB_USER'),
    'password' : os.environ.get('DB_PASSWORD'),
    'dbname' : os.environ.get('DB_NAME'),
    'host' : os.environ.get('DB_HOST'),
    'port' : os.environ.get('DB_PORT'),
}