# config.py
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    data =  {
        'host': str(os.getenv('DB_HOST')),
        'user': str(os.getenv('DB_USER')),
        'password': str(os.getenv('DB_PASSWORD')),
        'database': str(os.getenv('DB_NAME')),
        'key': str(os.getenv('AES_KEY')),
        'port': int(os.getenv('DB_PORT'))
    }
    return data
