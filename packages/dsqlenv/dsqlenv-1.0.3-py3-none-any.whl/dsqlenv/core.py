import pymysql
from .encryption import AESEncryptor
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.disabled = True

class SQL:
    def __init__(self, config={}):
        """
        init database connection
        :param config: database configuration
        """
        try:
            self.config = config
            self.host = self.get_config_from_cfg_or_env('host', 'DB_HOST')
            self.user = self.get_config_from_cfg_or_env('user', 'DB_USER')
            self.password = self.get_config_from_cfg_or_env('password', 'DB_PASSWORD')
            self.database = self.get_config_from_cfg_or_env('database', 'DB_NAME')
            self.port = int(self.get_config_from_cfg_or_env('port', 'DB_PORT', '3306'))
            self.table = self.get_config_from_cfg_or_env('table', 'TABLE_NAME', 'dagent_info')
            self.id_column = self.get_config_from_cfg_or_env('id_column', 'ID_COLUMN', 'name')
            self.info_column = self.get_config_from_cfg_or_env('info_column', 'INFO_COLUMN', 'data')
            # Init an AESEncryptor instance
            self.encryptor = AESEncryptor(self.get_config_from_cfg_or_env('key', 'AES_KEY'))

            # Connect to the database
            self.conn = pymysql.connect(
                host=self.host, user=self.user, password=self.password,
                database=self.database, charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor, port=self.port,
                connect_timeout=10  # 设置连接超时为10秒
            )
            self.cursor = self.conn.cursor()
            logger.info("Database connection established")
            self.create_table_if_not_exists()

        except Exception as e:
            logger.error(f"dsqlenv Database connection failed: {e}")
            raise e

    def create_table_if_not_exists(self):
        """Create table if it does not exist."""
        try:
            # check table
            sql = f"SHOW TABLES LIKE '{self.table}'"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            if result:
                logger.info(f"Table '{self.table}' exists")
                return
            else:
                # ask user if they want to create the table
                logger.info(f"Table '{self.table}' does not exist")
                create_table = input(f"Do you want to create table '{self.table}'? (yes/no): ")
                if create_table.lower() != 'yes':
                    return
            logger.info(f"Creating table '{self.table}'")
            # create table
            sql = f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                {self.id_column} VARCHAR(255) NOT NULL PRIMARY KEY,
                {self.info_column} BLOB NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            self.cursor.execute(sql)
            self.conn.commit()
            logger.info(f"Table '{self.table}' checked/created successfully")
        except Exception as e:
            logger.error(f"Failed to create table {self.table}: {e}")
            raise e

    def get_config_from_cfg_or_env(self, cfg_key, env_key, default=None):
        """
        Get configuration from config file or environment variable
        """
        if cfg_key in self.config:
            return self.config[cfg_key]
        elif env_key in os.environ:
            return os.environ[env_key]
        # 从~/.dsqlenv/.env文件中获取配置
        elif os.path.exists(os.path.expanduser('~/.dsqlenv/.env')):
            with open(os.path.expanduser('~/.dsqlenv/.env'), 'r') as f:
                for line in f:
                    if line.startswith(f"{env_key}="):
                        return line.split('=')[1].strip()
        else:
            if default:
                return default
            else:
                raise ValueError(f"Missing configuration: {cfg_key} or {env_key} not found")

    def get_data_by_id(self, id):
        """
        Get data by id from the database
        """
        try:
            sql = f"SELECT {self.info_column} FROM {self.table} WHERE {self.id_column} = %s"
            self.cursor.execute(sql, id)
            result = self.cursor.fetchone()
            if result:
                return self.encryptor.decrypt(result[self.info_column])
            else:
                return None
        except Exception as e:
            logger.error(f"Get data failed: {e}")
            print(f"Get data failed: {e}")
            raise e

    def insert_data(self, id, data, if_exists='replace'):
        """
        Insert or update data in the database
        """
        if self.get_data_by_id(id):
            if if_exists == 'replace':
                self.update_data(id, data)
                return
            elif if_exists == 'ignore':
                return
            else:
                raise ValueError(f"Invalid if_exists value: {if_exists}")
        try:
            sql = f"INSERT INTO {self.table} ({self.id_column}, {self.info_column}) VALUES (%s, %s)"
            self.cursor.execute(sql, (id, self.encryptor.encrypt(data)))
            self.conn.commit()
            logger.info("Insert data successfully")
        except Exception as e:
            logger.error(f"Insert data failed: {e}")
            raise e

    def update_data(self, id, data):
        """
        Update data in the database, if not exists, insert it
        """
        try:
            sql = f"REPLACE INTO {self.table} ({self.id_column}, {self.info_column}) VALUES (%s, %s)"
            self.cursor.execute(sql, (id, self.encryptor.encrypt(data)))
            self.conn.commit()
            logger.info("Update data successfully")
        except Exception as e:
            logger.error(f"Update data failed: {e}")
            raise e

    def delete_data(self, id):
        """
        Delete data from the database
        """
        try:
            sql = f"DELETE FROM {self.table} WHERE {self.id_column} = %s"
            self.cursor.execute(sql, id)
            self.conn.commit()
            logger.info("Delete data successfully")
        except Exception as e:
            logger.error(f"Delete data failed: {e}")
            raise e

    def close(self):
        """
        Close the cursor and connection explicitly
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            logger.info("Database connection closed")
        except Exception as e:
            logger.error(f"Failed to close database connection: {e}")
    
    def __del__(self):
        """
        Ensure that resources are cleaned up
        """
        try:
            self.close()  # Explicitly call the close function
        except Exception as e:
            logger.error(f"Error during __del__ cleanup: {e}")
