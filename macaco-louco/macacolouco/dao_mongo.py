from hashlib import sha256

from pymongo import MongoClient
from pymongo.collection import Collection
from bson import ObjectId


MONGODB_URI = "mongodb://pythonbrasil:pythonbrasil@localhost:27017"
MONGODB_DATABASE = "pythonbrasil"


class MongoDB:
    def __init__(self) -> None:
        client = MongoClient(MONGODB_URI)
        self.database = client[MONGODB_DATABASE]

    def get_object_id(self, value: str) -> ObjectId:
        return ObjectId(sha256(value.encode()).hexdigest()[:12].encode())

    def products(self) -> Collection:
        return self.database["products"]

    def recommendations(self) -> Collection:
        return self.database["recommendations"]
