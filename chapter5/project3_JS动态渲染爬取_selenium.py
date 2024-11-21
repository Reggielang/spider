import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO)

INDEX_URL = 'https://spa2.scrape.center/page/{page}'

TIME_OUT=10
TOTAL_PAGE = 10
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, TIME_OUT)




RESULTS_DIR = 'results2'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

def scrape_page(url,condition,locator):
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url)

def scrape_index(page):
    url = INDEX_URL.format(page=page)
    return scrape_page(url,EC.visibility_of_element_located,(By.CSS_SELECTOR,'#index .item'))

def parse_index():
    data_list = browser.find_elements(By.XPATH,"//div[@id='index']//div[contains(@class, 'item')]//a[contains(@class, 'a')]")
    for data in data_list:
        href = data.get_attribute('href')
        yield urljoin(INDEX_URL,href)


def scrape_detail(url):
    return scrape_page(url,EC.visibility_of_element_located,(By.TAG_NAME,'h2'))

def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.TAG_NAME,'h2').text
    category = [element.text for element in browser.find_elements(By.CSS_SELECTOR,'.categories button span')]
    cover = browser.find_element(By.CSS_SELECTOR,'.cover').get_attribute('src')
    score = browser.find_element(By.CSS_SELECTOR,'.score').text
    drama = browser.find_element(By.CSS_SELECTOR,'.drama p').text
    return {
        'url': url,
        'name': name,
        'category': category,
        'cover': cover,
        'score': score,
        'drama': drama,
    }


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.txt'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls= parse_index()
            # 返回的是一个生成器对象，需要转化为list才能进行迭代
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                logging.info('detail data %s', detail_data)
                save_data(detail_data)
    finally:
        browser.close()




if __name__ == '__main__':
    main()