import unittest
import os
from dsqlenv.core import SQL

class TestSQL(unittest.TestCase):

    def setUp(self):
        # 设置测试配置
        self.config = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'user': os.getenv('DB_USER', 'root'),
            'password': os.getenv('DB_PASSWORD', 'password'),
            'database': os.getenv('DB_NAME', 'test_db'),
            'key': os.getenv('AES_KEY', 'test_key'),
            'table': 'dagent_info',
            'id_column': 'name',
            'info_column': 'data'
        }
        print(self.config)
        # 初始化 SQL 实例
        self.sql = SQL()

    def test_init(self):
        # 测试 SQL 初始化是否正确
        self.assertEqual(self.sql.table, self.config['table'])

    def test_get_data_by_id(self):
        # 假设数据库中已经有数据 'test_id'
        result = self.sql.get_data_by_id('test_id')
        self.assertIsNotNone(result)
        print(f"Data for 'test_id': {result}")

    def test_insert_data(self):
        # 插入测试数据
        self.sql.insert_data('new_id', 'test_data')
        result = self.sql.get_data_by_id('new_id')
        self.assertEqual(result, 'test_data')
        print(f"Inserted data: {result}")

    def test_update_data(self):
        # 更新数据
        self.sql.update_data('new_id', 'updated_data')
        result = self.sql.get_data_by_id('new_id')
        self.assertEqual(result, 'updated_data')
        print(f"Updated data: {result}")

    def test_delete_data(self):
        # 删除数据
        self.sql.delete_data('new_id')
        result = self.sql.get_data_by_id('new_id')
        self.assertIsNone(result)
        print(f"Data after deletion: {result}")

if __name__ == '__main__':
    unittest.main()
