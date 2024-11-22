from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time


BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, 'login')
INDEX_URL = urljoin(BASE_URL, 'page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

browser = webdriver.Chrome()
browser.get(BASE_URL)
browser.find_element(By.CSS_SELECTOR,'input[name="username"]').send_keys(USERNAME)
browser.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys(PASSWORD)
browser.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
time.sleep(5)

#从浏览器对象中取出cookie信息
cookies = browser.get_cookies()
print(cookies)
browser.close()

#cookie放入请求中
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'],cookie['value'])

resp_index = session.get(INDEX_URL)
print(resp_index.status_code,resp_index.url)