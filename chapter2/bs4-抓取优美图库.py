# 1.拿到主页面的源代码，然后提取子页面的链接地址
# 2. 通过子页面的链接地址，拿到子页面的源代码，然后提取图片的下载地址
# 3. 下载图片
import requests
from bs4 import BeautifulSoup
import time
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
    # 拿到子页面的源代码
    child_page_resp = requests.get(image_url, headers=headers)
    #从子页面中提取图片的下载地址
    child_page = BeautifulSoup(child_page_resp.text, "html.parser")
    image_src = child_page.find("img", class_="preview img-fluid")
    # print(image_src)
    final_image_url = image_src.get("data-src")
    print(final_image_url)
    # 下载图片
    image_resp = requests.get(final_image_url, headers=headers)
    # 这里拿到的是字节
    # image_resp.content
    # 把图片内容写入文件
    file_name = final_image_url.split("/")[-1]
    with open("images/" + file_name+'.png', "wb") as f:
        f.write(image_resp.content)
    print(f"图片下载成功{file_name}")
    time.sleep(1)

