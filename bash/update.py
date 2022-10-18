from get_mongodb_connect import mongoDBClient

if __name__ == "__main__":
    col = "test_collection2"
    # 修改前数据
    for x in mongoDBClient[col].find():
        print(x)
    print()

    # 修改第一条匹配到的记录
    query = {"alexa": "10"}
    new_values = {"$set": {"alexa": "123"}}
    result = mongoDBClient[col].update_one(query, new_values)
    print(result)
    # 输出修改后集合
    for x in mongoDBClient[col].find():
        print(x)
    print()

    # 修改所有匹配到的记录
    query = {"name": {"$regex": "^F"}}
    new_values = {"$set": {"alexa": "125"}}
    x = mongoDBClient[col].update_many(query, new_values)
    print(f"文档已修改 {x.modified_count} 条记录")
    # 输出修改后集合
    for x in mongoDBClient[col].find():
        print(x)
    print()
