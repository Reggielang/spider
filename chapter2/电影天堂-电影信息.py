# 1. 定位到2024必看片
# 2. 从2024必看片中提取到子页面的链接地址
# 3. 请求子页面的链接地址，拿到电影的下载地址
import re

import requests
from doc.pycurl.examples.quickstart.response_headers import headers

from chapter2.豆瓣TOP250 import result

domain = "https://dytt89.com"
header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "cookie":"__51uvsct__KSHU1VNqce379XHB=1; __51vcke__KSHU1VNqce379XHB=cec240ca-02f9-5055-8999-17cc530e5638; __51vuft__KSHU1VNqce379XHB=1731047094563; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1731047095; HMACCOUNT=29CFA9AE44F4D279; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1731047095; Hm_lvt_8e745928b4c636da693d2c43470f5413=1731047095; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%227220bf17-7def-5fb8-a4d5-5d640f788c00%22%2C%20%22vd%22%3A%204%2C%20%22stt%22%3A%201313501%2C%20%22dr%22%3A%2025364%2C%20%22expires%22%3A%201731050208062%2C%20%22ct%22%3A%201731048408062%7D; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1731048409; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1731048409; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1731048409",
    }
# verify=False 去掉安全验证
resp = requests.get(domain, headers=header,verify=False)
# 该网站用的gb2312
resp.encoding = "gb2312"
# print(resp.text)


#主页面解析拿到ul里面的li
obj = re.compile(r"2024必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)

#解析结果并获取子页面链接
ul_obj = re.compile(r"<li>.*?<a href='(?P<item_url>.*?)'",re.S)

# 子页面的下载地址
movie_obj = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?'
                       r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_url>.*?)">',re.S)


result = obj.finditer(resp.text)
child_url_li = []

for it in result:
    # print(it.group("ul"))
    ul = it.group("ul")
    find_url = ul_obj.finditer(it.group("ul"))
    # 提取子页面的链接
    for i in find_url:
        # print(i.group("item_url"))
        # 拼接子页面的链接
        child_url = domain+i.group("item_url")
        child_url_li.append(child_url)

resp.close()

# 提取子页面
for url in child_url_li:
    print(url)
    child_resp = requests.get(url,headers=header)
    child_resp.encoding = "gb2312"
    # # 提取下载地址
    # print(child_resp.text)
    movie = movie_obj.search(child_resp.text)
    print(movie.group("movie"))
    print(movie.group("download_url"))