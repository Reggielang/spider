# 代理,通过第三方的机器去发送请求

import requests

# resp = requests.get("https://www.baidu.com")
# resp.encoding = "utf-8"
# print(resp.text)

# 免费代理IP网站
# https://www.zdaye.com/free/?ip=&adr=&checktime=&sleep=&cunhuo=&dengji=4&nadr=&https=&yys=&post=&px=

proxies = {
    "http":"",
    "https":"111.1.61.49:3128",
}

resp2 = requests.get("https://www.baidu.com",proxies=proxies)
resp2.encoding = "utf-8"
print(resp2.text)