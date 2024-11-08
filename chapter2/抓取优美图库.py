# 1.拿到主页面的源代码，然后提取子页面的链接地址
import requests
from bs4 import BeautifulSoup
url = "https://www.dailybing.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)

main_page = BeautifulSoup(resp.text, "html.parser")
# 把抓取范围第一次缩小
# print(main_page.find_all("div", class_="image-item"))
image_list = main_page.find_all("a", class_="shadow")

# 拿到子页面的链接地址
for item in image_list:
    image_url = item.get("href")
    print(image_url)
