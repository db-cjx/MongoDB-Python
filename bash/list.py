from get_mongodb_connect import mongoDBClient
if __name__ == "__main__":
    # 查询一条数据
    col = "test_collection"
    result = mongoDBClient[col].find_one()
    print(result)
    print()

    # 查询集合中所有数据
    col = "test_collection2"
    result = mongoDBClient[col].find()
    for i in result:
        print(i)
    print()

    # 查询指定字段的数据
    result = mongoDBClient[col].find({}, {"_id": 0, "name": 1, "alexa": 1})
    for i in result:
        print(i)
    print()

    col = "test_collection2"
    # 根据指定条件查询
    query = {"name": "Github"}
    result = mongoDBClient[col].find(query)
    for i in result:
        print(i)
    print()

    # 高级查询 $gt:大于
    query = {"alexa": {"$gt": "101"}}
    result = mongoDBClient[col].find(query)
    for i in result:
        print(i)
    print()

    # 使用正则表达式查询
    query = {"name": {"$regex": "^G"}}
    result = mongoDBClient[col].find(query)
    for i in result:
        print(i)
    print()

    # 返回指定条数记录
    result = mongoDBClient[col].find().limit(3)
    for i in result:
        print(i)
    print()

    # 对字段 alexa 按升序排序
    result = mongoDBClient[col].find().sort("alexa")
    for i in result:
        print(i)
    print()

    # 对字段 alexa 按降序排序
    result = mongoDBClient[col].find().sort("alexa", -1)
    for i in result:
        print(i)
    print()
