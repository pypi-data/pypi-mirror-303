from typing import Any
import pandas as pd
import json
from pymongo import MongoClient


class MongoOperation:
    _collection = None  # Protected variable
    _database = None

    def __init__(self, client_url: str, database_name: str, collection_name: str = None):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name
    def create_mongo_client(self):
        """Create a MongoDB client."""
        return MongoClient(self.client_url)

    def create_database(self):
        """Create or get the database."""
        if self._database is None:
            client = self.create_mongo_client()
            self._database = client[self.database_name]
        return self._database

    def create_collection(self):
        """Create or get the collection."""
        if self._collection is None:
            database = self.create_database()
            self._collection = database[self.collection_name]
        return self._collection

    def insert_record(self, record: dict, collection_name: str) -> Any:
        collection = self.create_collection()
        if isinstance(record, list):
            for data in record:
                if not isinstance(data, dict):
                    raise TypeError("Record must be a dictionary or a list of dictionaries.")
            collection.insert_many(record)
        elif isinstance(record, dict):
            collection.insert_one(record)

    def bulk_insert(self, datafile: str, collection_name: str = None):
        """Bulk insert records from a file into the specified collection."""
        self.path = datafile
        if self.path.endswith('.csv'):
            dataframe = pd.read_csv(self.path, encoding='utf-8')
        elif self.path.endswith(".xlsx"):
            dataframe = pd.read_excel(self.path, encoding='utf-8')
        else:
            raise ValueError("Unsupported file format. Please use .csv or .xlsx.")
        datajson = json.loads(dataframe.to_json(orient='records'))
        collection = self.create_collection()
        collection.insert_many(datajson)
