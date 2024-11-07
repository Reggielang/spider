# 1. 定位到2024必看片
# 2. 从2024必看片中提取到子页面的链接地址
# 3. 请求子页面的链接地址，拿到电影的下载地址
import re

import requests
from doc.pycurl.examples.quickstart.response_headers import headers

from chapter2.豆瓣TOP250 import result

domain = "https://dytt89.com/"
header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "cookie":"__51uvsct__KSHU1VNqce379XHB=1; __51vcke__KSHU1VNqce379XHB=c55bfe45-8f6d-5a1a-9731-773dd1d26048; __51vuft__KSHU1VNqce379XHB=1730985737856; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1730985738; HMACCOUNT=C6C60C414979E4A6; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1730985738; Hm_lvt_8e745928b4c636da693d2c43470f5413=1730985738; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22ddbcd609-917c-5bf0-8300-25e9b49f0845%22%2C%20%22vd%22%3A%205%2C%20%22stt%22%3A%201090129%2C%20%22dr%22%3A%20168563%2C%20%22expires%22%3A%201730988627984%2C%20%22ct%22%3A%201730986827984%7D; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1730986828; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1730986828; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1730986828"}
# verify=False 去掉安全验证
resp = requests.get(domain, headers=header,verify=False)
# 该网站用的gb2312
resp.encoding = "gb2312"
# print(resp.text)

#主页面解析拿到ul里面的li
obj = re.compile(r"2024必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)

#解析结果并获取子页面链接
ul_obj = re.compile(r"<li>.*?<a href='(?P<item_url>.*?)'",re.S)

result = obj.finditer(resp.text)

for it in result:
    # print(it.group("ul"))
    ul = it.group("ul")
    find_url = ul_obj.finditer(it.group("ul"))
    # 提取子页面的链接
    for i in find_url:
        print(i.group("item_url"))
