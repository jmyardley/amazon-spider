# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.exceptions import DropItem
import logging
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

#class AmazonspiderPipeline:
#    def process_item(self, item, spider):
#        return item

class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.collection1 = db[settings['MONGODB_COLLECTION1']]
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("missing {0}".format(data))
        if valid:
            if item.get('msrp'):
                self.collection1.insert(dict(item))
                print("product added")
                
                product = self.collection1.find()
                self.collection.update_many({'productid': ''}, {'$set': {'productid': product[0]['_id']}})
            else:
                self.collection.insert(dict(item))
                print("added")
        return item
        