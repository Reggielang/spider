import asyncio
import json

import aiohttp
import logging

import pandas as pd
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO)

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUM = 100
CONCURRENCY = 10

#MONGODB
MONGO_URL = 'mongodb://localhost:27017/'
MONGO_DB = 'books'
MONGO_COLLECTION = 'books'

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

semanphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api(url):
    async with semanphore:
        try:
            logging.info('scraping %s...', url)
            async with session.get(url) as response:
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url)

async def scrape_index(page):
    url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
    return await scrape_api(url)

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUM + 1)]
    resp = await asyncio.gather(*scrape_index_tasks)
    logging.info('result is %s', json.dumps(resp, indent=2))

    ids=[]
    for index_data in resp:
        if not index_data:continue
        for item in index_data['results']:
            ids.append(item['id'])


    scrape_details_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]
    await asyncio.wait(scrape_details_tasks)
    await session.close()


async def save_data(data):
    logging.info('saving data %s', data)
    if data:
        return await collection.update_one({'id': data['id']}, {'$set': data}, upsert=True)

async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    await save_data(data)

if __name__ == '__main__':
    asyncio.run(main())
