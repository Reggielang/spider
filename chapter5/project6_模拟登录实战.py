import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, 'login')
INDEX_URL = urljoin(BASE_URL, 'page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

# 模拟登录获取cookie
resp_login = requests.post(LOGIN_URL,data={
    'username':USERNAME,
    'password':PASSWORD
},allow_redirects=False)
cookies = resp_login.cookies
print("cookies",cookies)

resp_index = requests.get(INDEX_URL,cookies=cookies)
print(resp_index.status_code,resp_index.url)


#使用session
session = requests.Session()
resp_login = session.post(LOGIN_URL,data={
    'username':USERNAME,
    'password':PASSWORD
})

cookies = session.cookies
print("cookies",cookies)
resp_index = session.get(INDEX_URL)
print(resp_index.status_code,resp_index.url)