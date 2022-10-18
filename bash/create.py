from get_mongodb_connect import mongoDBClient


def createCollection(col_name: str):
    return mongoDBClient[col_name]


if __name__ == "__main__":
    col_name = "test_collection23"
    col = createCollection(col_name)
    print(col)
