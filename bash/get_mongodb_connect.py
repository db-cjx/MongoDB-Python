import pymongo


mongodb_config = {
    "host": "192.168.122.251",
    "port": 27017,
    "database": "klb",
    "user": "mongouser",
    "password": "mongopswd"
}


def getMongoDBConnect(mongodbName):
    host = mongodb_config["host"]
    port = mongodb_config["port"]
    user = mongodb_config["user"]
    password = mongodb_config["password"]
    database = mongodb_config["database"]
    client = pymongo.MongoClient(f'mongodb://{user}:{password}@{host}:{port}/')
    db = client[database]
    return db


mongoDBClient = getMongoDBConnect("default")