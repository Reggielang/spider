import requests
url = "https://fanyi.baidu.com/sug"

s = input("请输入翻译的单词")

dat = {
    "kw":s
}
resp = requests.post(url,data=dat)

print(resp)
print(resp.json())