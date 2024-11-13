import aiohttp
import asyncio

import requests
from bs4 import BeautifulSoup
import time

from win32comext.shell.demos.servers.folder_view import tasks

urls = [
    "https://dailybing.com/api/v1/20241112zh-cnFHD1360",
    "https://dailybing.com/api/v1/20241111zh-cnFHD1360",
    "https://dailybing.com/api/v1/20241110zh-cnFHD1360",
]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


async def aiodownload(url):
    name = url.split("/")[-1]
    #发送异步请求
    async with aiohttp.ClientSession() as session:
        # 得到图片
        async with session.get(url) as resp:
            resp.content.read()
            # 保存到文件
            with open("images/" + name + ".png", "wb") as f:
                f.write(await resp.content.read()) #读取内容也是异步的

    print(name,"下载完成")
async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())