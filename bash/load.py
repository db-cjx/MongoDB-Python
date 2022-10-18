from read import read
from get_mongodb_connect import mongoDBClient
def load(col, data_source_uid):
    result = read(data_source_uid)
    return mongoDBClient[col].insert_many(result)


if __name__ == "__main__":
    col = "student2"
    # load(col, 'f63946fa-ef31-4524-b221-aa8078521428')
    # load(col, '41d22a91-b5b1-474b-a95c-cc417fff8650')
    load(col, "d73f3496-b9dc-4830-88d4-f0954d04166e")
    for i in mongoDBClient[col].find():
        print(i)
