from get_mongodb_connect import mongoDBClient

def insert_one_documents(col, data):
    return mongoDBClient[col].insert_one(data)


def insert_many_documents(col, data_list):
    return mongoDBClient[col].insert_many(data_list)


if __name__ == "__main__":
    col_name = "test_collection"
    col_name2 = "test_collection2"
    data = {
        "author": "Mike",
        "tags": ["mongodb", "python", "pymongo"],
    }
    data_list = [
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"},
    ]
    insert_one_id = insert_one_documents(col_name, data)
    insert_many_id = insert_many_documents(col_name2, data_list)
    print(insert_one_id)
    print(insert_many_id)
