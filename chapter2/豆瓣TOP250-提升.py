# 分析请求页面 # 1. 服务器渲染： 在服务器端直接把数据和HTML整合输出，然后统一返回给浏览器 （在页面源代码中能看到数据）
# 服务器渲染，直接页面源代码中解析数据

import requests
import  re
import csv
url = "https://movie.douban.com/top250"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}


# param = {
#     "start": 25,
# }
# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)人评价</span>',re.S)

# 存入文件
f = open("data.csv", mode="w", encoding='utf-8')
csvwriter = csv.writer(f)

for num in range(0,250,25):
    new_url = url+f'?start={num}'
    resp = requests.get(new_url,headers=header)
    page_content = resp.text
    result = obj.finditer(page_content)
    for i in result:
        # print(i.group("year").strip())
        # print(i.group("score"))
        # print(i.group("num"))
        # print(i.group("name"))
        # print(i.groupdict())
        dic = i.groupdict()
        dic["year"] = dic["year"].strip()
        csvwriter.writerow(dic.values())
    print(f"解析结束----{num}")

f.close()
print("解析结束")



