import requests
import logging
import pymongo
# url = "https://spa1.scrape.center/"


logging.basicConfig(level=logging.INFO)

# 保存数据MONGODB
MONGO_URL = 'mongodb://localhost:27017/'
# MONGO_DB = 'movie'
# MONGO_COLLECTION = 'movies'

client = pymongo.MongoClient(MONGO_URL)
db = client['movie']
collection = db['movies']


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        logging.error('get invalid status code %s while scraping %s', resp.status_code, url)
    except:
        logging.error('error occurred while scraping %s', url, exc_info=True)

def scrape_index(page):
    limit = 10
    index_url = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
    url = index_url.format(limit=limit, offset=(page - 1) * limit)
    return scrape_page(url)

def scrape_detail(id):
    detail_url = 'https://spa1.scrape.center/api/movie/{id}'
    return scrape_page(detail_url.format(id=id))

def save_data(data):
    collection.update_one({'id': data.get('id')}, {'$set': data}, upsert=True)


if __name__ == '__main__':
    total = 10
    for page in range(1,total+1,1):
        index_data= scrape_index(page)
        for item in index_data['results']:
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail-data %s',detail_data)
            save_data(detail_data)
            logging.info('data saved successfully!')
