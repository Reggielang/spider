import requests
from urllib.parse import urljoin

BASE_URL = 'https://login3.scrape.center/'
LOGIN_URL = urljoin(BASE_URL, '/api/login')
INDEX_URL = urljoin(BASE_URL, '/api/book')
USERNAME = 'admin'
PASSWORD = 'admin'

# 模拟登录获取cookie
resp_login = requests.post(LOGIN_URL,json={
    'username':USERNAME,
    'password':PASSWORD
})

data = resp_login.json()

print("data",data)
jwt = data.get('token')
print("jwt:",jwt)

headers = {
    'Authorization':f'jwt {jwt}'
}

resp_index = requests.get(INDEX_URL,params={'limit':18,'offset':0},headers=headers)
print(resp_index.status_code,resp_index.url,resp_index.json())
