import json
import asyncio

import pyppeteer
from pyppeteer import launch
import logging
from urllib.parse import urljoin
from os import makedirs
from os.path import exists
from pyppeteer.errors import TimeoutError

logging.basicConfig(level=logging.INFO)

TIME_OUT=10
TOTAL_PAGE = 10
HEADLESS = False
WINDOW_WIDTH,WINDOW_HEIGHT = 1366, 768
browser,tab = None,None
INDEX_URL = 'https://spa2.scrape.center/page/{page}'



RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

async def init():
    global browser,tab
    browser = await launch(headless=HEADLESS, args=['--hide-scrollbars',f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})

async def scrape_page(url,selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector,options={'timeout':TIME_OUT*1000})
    except TimeoutError:
        logging.error('error occurred while scraping %s', url)

async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')

async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')

async def scrape_detail(url):
    await  scrape_page(url,'h2')

async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.innerText')
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.innerText')
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama,
    }

async def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.txt'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            logging.info('get index data %s', detail_urls)
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info('get detail data %s', detail_data)
                await save_data(detail_data)
    finally:
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())