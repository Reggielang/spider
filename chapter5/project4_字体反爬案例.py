from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re
import requests


url = 'https://antispider4.scrape.center/css/app.654ba59e.css'

resp = requests.get(url)
pattern = re.compile(r'.icon-(.*?):before\{content:"(.*?)"\}')
results = re.findall(pattern,resp.text)
icon_map = {item[0]:item[1] for item in results}

def prase_score(item):
    elements = item('.icon')
    icon_values = []
    for element in elements.items():
        class_name = (element.attr('class'))
        icon_key = re.search('icon-(\\d+)',class_name).group(1)
        icon_value = icon_map.get(icon_key)
        icon_values.append(icon_value)
    return ''.join(icon_values)

print("开始运行了？")
browser = webdriver.Edge()
browser.get('https://antispider4.scrape.center/')
WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.item')))
html = browser.page_source
doc = pq(html)
items = doc('.item')
for item in items.items():
    name = item('.name').text()
    categories = [o.text() for o in item('.categories button').items()]
    socre = prase_score(item)
    print(f'name:{name} categories:{categories} socre:{socre}')
browser.close()