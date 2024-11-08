
# 1. 拿到页面源代码
# 使用bs4进行解析，拿到数据

import requests
from bs4 import BeautifulSoup
url = "http://www.xinfadi.com.cn/getCat.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

# 不同的参数可以获得不同的数据
# prodCatid: 1190
# prodCatid: 1189
param = {
    "prodCatid": 1187,
}
resp = requests.get(url,headers=headers,params=param)

print(resp.json())


# 解析数据
# 1. 页面源代码交给beautifulsoup进行处理，生成bs对象
# 2. 从bs对象中查找数据
# find(标签名,属性=值)
# find_all(标签名,属性=值)
url2 = "http://www.xinfadi.com.cn/index.html"
resp = requests.get(url2,headers=headers)
page = BeautifulSoup(resp.text,"html.parser")
# table = page.find("div",class_="tbl-header")
table = page.find("div",attrs={"class":"tbl-header"})
print(table)










