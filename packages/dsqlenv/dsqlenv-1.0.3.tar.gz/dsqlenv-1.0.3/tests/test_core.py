# test_core.py
import unittest
from dsqlenv.core import SQL
from dsqlenv.config import load_config

class TestSQL(unittest.TestCase):
    def setUp(self):
        config = load_config()
        self.db = SQL(config)

    def test_insert_and_get(self):
        self.db.insert_data('test_id', 'test_data')
        data = self.db.get_data_by_id('test_id')
        self.assertEqual(data, 'test_data')

    def test_update(self):
        self.db.insert_data('test_id', 'test_data')
        self.db.update_data('test_id', 'new_data')
        data = self.db.get_data_by_id('test_id')
        self.assertEqual(data, 'new_data')
    
    def test_delete(self):
        self.db.insert_data('test_id', 'test_data')
        self.db.delete_data('test_id')
        data = self.db.get_data_by_id('test_id')
        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
