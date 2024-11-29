# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from elasticsearch import Elasticsearch
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class ScrapyitempiplinedemoPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):

    def __init__(self, mongo_url, mongo_db, mongo_collection):
        self.mongo_url = mongo_url
        self.database = mongo_db
        self.collection = mongo_collection
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.database]


    def process_item(self, item, spider):
        self.db[self.collection].update_one({'name':item['name']}, {'$set':dict(item)}, upsert=True)
        return item

    def close_spider(self, spider):
        self.client.close()


class ElasticSearchPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        cls.es_url = crawler.settings.get("ES_URL")
        cls.es_index = crawler.settings.get("ES_INDEX")
        return cls()

    def open_spider(self, spider):
        self.es = Elasticsearch([self.es_url])
        if not self.es.indices.exists(index = self.es_index):
            self.es.indices.create(index = self.es_index)

    def process_item(self, item, spider):
        self.es.index(index=self.es_index, body=dict(item),id=hash(item['name']))
        return item

    def close_spider(self, spider):
        self.es.transport.close()


class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        movie = request.meta['movie']
        type = request.meta['type']
        name = request.meta['name']
        file_name = f'{movie}/{type}/{name}.jpg'
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

    def get_media_requests(self, item, info):
        for director in item['directors']:
            director_name = director['name']
            director_image = director['image']
            yield Request(director_image, meta={'movie': item['name'], 'type': 'director', 'name': director_name})

        for actor in item['actors']:
            actor_name = actor['name']
            actor_image = actor['image']
            yield Request(actor_image, meta={'movie': item['name'], 'type': 'actor', 'name': actor_name})
