# 拿页面源代码
# 提取和解析数据
from lxml import etree

import requests

url = "https://www.zbj.com/fw/?k=saas"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "cookie":"_uq=1f1d7d1ef8c1423fbd6c301c4164ce07; uniqid=d01m89gx7s51mp; _suq=5c497132-17ca-42e6-b387-6b5319482032; oldvid=; vid=b9e195156ea7fc43f9b48afd140829dc; Hm_lvt_a360b5a82a7c884376730fbdb8f73be2=1731292360; HMACCOUNT=29CFA9AE44F4D279; nsid=s%3AQfyJ9g3k08wLyYvM00Vg0bm7cCCxcVeN.RNWIpDnNd0jQg7rkuMQt9xdxmeFsTC8ejeQHVwXkVFk; unionJsonOcpc=eyJvdXRyZWZlcmVyIjoiaHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPVlIWnV6Y1U5RUhQTkhjaFQzVEwiLCJwbWNvZGUiOiIifQ==; local_city_path=chengdu; local_city_name=%E6%88%90%E9%83%BD; local_city_id=3829; vidSended=1; Hm_lpvt_a360b5a82a7c884376730fbdb8f73be2=1731292384; s_s_c=xhA3dh7QsA2lgP8ro4tGR5DcQp2Fhvtaw8F%2BEOF%2FWxkYEMljNWLfIfPDl9h9dsoTleMje0HjL45RvSTJK97CuQ%3D%3D"

}
resp = requests.get(url,headers=headers)

# 解析
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div')
print(divs)
# 每一个服务商的信息
for div in divs:
   price=div.xpath('./div/div[3]/div[1]/span/text()')[0].strip("¥")
   title=div.xpath('./div/div[3]/div[2]/a/span/text()')[0]
   com_name=div.xpath('./div/div[5]/div/div/div/text()')[0]
   print(price,title,com_name)



