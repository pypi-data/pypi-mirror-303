import os
from dsqlenv.core import SQL

sql = SQL()


def test_get_data_by_id():
    # 假设数据库中已经有数据 'test_id'
    result = sql.get_data_by_id('test_id')
    if result is not None:
        print(f"Data for 'test_id': {result}")
    else:
        print("Data Retrieval Test Failed!")

def test_insert_data():
    # 插入测试数据
    sql.insert_data('new_id', 'test_data')
    result = sql.get_data_by_id('new_id')
    if result == 'test_data':
        print(f"Inserted data: {result}")
    else:
        print("Data Insertion Test Failed!")

def test_update_data():
    # 更新数据
    sql.update_data('new_id', 'updated_data')
    result = sql.get_data_by_id('new_id')
    if result == 'updated_data':
        print(f"Updated data: {result}")
    else:
        print("Data Update Test Failed!")

def test_delete_data():
    # 删除数据
    sql.delete_data('new_id')
    result = sql.get_data_by_id('new_id')
    if result is None:
        print(f"Data after deletion: {result}")
    else:
        print("Data Deletion Test Failed!")

if __name__ == '__main__':
    test_get_data_by_id()
    # test_insert_data()
    # test_update_data()
    # test_delete_data()
    # print("All tests completed.")
