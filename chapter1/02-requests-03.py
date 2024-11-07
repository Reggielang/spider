import requests

url = "https://movie.douban.com/j/chart/top_list?"
# 重新封装参数
# start 参数：从0开始，每次加20，可以爬到N多数据
param={
    "type": "24",
    "interval_id": "100:90",
    "action":"",
    "start": 0,
    "limit": 20,
}

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

resp = requests.get(url,params=param,headers=header)

print(resp.request.url)
print(resp.request.headers)
print(resp.json())
resp.close() # 关闭连接