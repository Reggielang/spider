# 登陆 - 得到cookie
#  带着cookie 去请求到书架URL - 书架上的内容

# 必须要把上面的请求连起来
# 我们可以使用session进行请求 - session可以认为是一连串的请求，在这个过程中cookie不会丢失
import requests

# 会话
session = requests.session()

# 1.登陆
url = "https://m.ydxrf.com/api/login"
data = {
    "username":"qq819343713",
    "password":"qq819343713"
}
resp = session.post(url=url,data=data)
# print(resp.text)
token = resp.json()['data']['token']
print(resp.json(),token)


data = {
    "token":f"{token}"
}
# 2.拿书架上的数据
# 刚才的那个session中是有cookie的 - 但是本次的请求是以上次请求的响应中的token作为验证 --所以请求的参数中加上token
resp = session.post("https://m.ydxrf.com/api/findBook",params=data)
print(resp.json())
