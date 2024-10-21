from typing import Dict, Any, List

from pymongo import UpdateOne

from buco_db_controller.mongo_db.mongo_db import MongoDB


class MongoDBBaseRepository(MongoDB):
    def __init__(self, db_name):
        super().__init__(db_name)

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document).inserted_id

    def insert_many_documents(self, collection_name, documents):
        collection = self.db[collection_name]
        return collection.insert_many(documents).inserted_ids

    def find_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find_documents(self, collection_name: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        collection = self.db[collection_name]
        return list(collection.find(query))

    def update_document(self, collection_name, query, update):
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': update}).modified_count

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query).deleted_count

    def upsert_document(self, collection_name, item):
        collection = self.db[collection_name]

        query = {'parameters': item['parameters']}
        update = {'$set': item}

        result = collection.update_one(query, update, upsert=True)
        return result.raw_result if result else None

    def bulk_upsert_documents(self, collection_name, data):
        collection = self.db[collection_name]
        operations = []

        for item in data:
            query = {'parameters': item['parameters']}
            update = {'$set': item}
            operations.append(UpdateOne(query, update, upsert=True))

        if operations:
            result = collection.bulk_write(operations)
            return result.bulk_api_result

        return None
