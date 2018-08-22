import base64
import datetime
import pprint
import random
import time
import uuid

import pymongo

class MongoDBTest:
    def __init__(self, mongo_host, mongo_port):
        self.client = pymongo.MongoClient(mongo_host, mongo_port)
        self.db = "mongo_test"
        self.collection = "collection_1"
        self.name_list = ["Hua", "Yuming"]
        self.tag_list = ["mongodb", "postgresql", "mssql", "mysql", "samba", "nfs", "webmail"]
        
    def _gen_random_name(self):
        return self.name_list[random.randint(0, len(self.name_list)-1)]
    
    def _gen_random_tag(self):
        return self.tag_list[random.randint(0, len(self.tag_list)-1)]

    def _gen_doc_dict(self):
        doc_dict = {
            "author": self._gen_random_name(),
            "uuid": str(uuid.uuid4()),
            "tag": self._gen_random_tag(),
            "date": datetime.datetime.utcnow()}
        return doc_dict
    
    def mongo_insert_one(self):
        db = self.client[self.db]
        collection = db[self.collection]
        one_doc = self._gen_doc_dict()
        mongo_uid = collection.insert_one(one_doc).inserted_id
        #print(mongo_uid)
        return
    
    def mongo_query(self):
        db = self.client[self.db]
        collection = db[self.collection]
        res = collection.find({"author": "Yuming"})
        for r in res:
            pprint.pprint(r)
        return

if __name__ == "__main__":
    myMongoDBTest = MongoDBTest("192.168.7.73", 27017)
    while True:
        myMongoDBTest.mongo_query()
        time.sleep(1)
