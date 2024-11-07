# 分析请求页面 # 1. 服务器渲染： 在服务器端直接把数据和HTML整合输出，然后统一返回给浏览器 （在页面源代码中能看到数据）
# 服务器渲染，直接页面源代码中解析数据

import requests
import  re
url = "https://movie.douban.com/top250"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

resp = requests.get(url,headers=header)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                 r'.*?',re.S)
result = obj.finditer(page_content)

for i in result:

    print(i.group("year").strip())
    print(i.group("name"))