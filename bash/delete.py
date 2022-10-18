from get_mongodb_connect import mongoDBClient

if __name__ == "__main__":
    col = "test_collection2"
    # 删除前数据
    for x in mongoDBClient[col].find():
        print(x)
    print()

    # 删除第一条匹配到的文档
    query = {"name": "Taobao"}
    mongoDBClient[col].delete_one(query)
    # 删除后输出
    for x in mongoDBClient[col].find():
        print(x)
    print()

    # 删除所有匹配到的文档
    query = {"name": {"$regex": "^F"}}
    x = mongoDBClient[col].delete_many(query)
    print(f"文档已删除 {x.deleted_count} 条记录")
    # 输出修改后集合
    for x in mongoDBClient[col].find():
        print(x)
    print()

    # 删除集合中的所有文档
    x = mongoDBClient[col].delete_many({})
    print(f"文档已删除 {x.deleted_count} 条记录")
    # 输出修改后集合
    for x in mongoDBClient[col].find():
        print(x)
    print()

    # 查询所有集合
    for x in mongoDBClient.list_collections():
        print(x)
    print()

    # 删除集合
    x = mongoDBClient[col].drop()
    print(x)

    # 查询所有集合
    for x in mongoDBClient.list_collections():
        print(x)
    print()
