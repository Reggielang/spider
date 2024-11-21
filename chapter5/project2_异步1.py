import asyncio

import aiohttp
import requests
import logging
import time

#不用协程
# total_number = 3
#
# url = "https://www.httpbin.org/delay/5"
#
# logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')
#
# start_time = time.time()
# for _ in range(1,total_number+1):
#     logging.info('scraping %s', url)
#     resp = requests.get(url)
#
# end_time = time.time()
# logging.info('total time: %s', end_time-start_time)

# start_time = time.time()
# async def get(url):
#     session = aiohttp.ClientSession()
#     resp = await session.get(url)
#     await resp.text()
#     await session.close()
#     return resp
# async def request():
#     # url = "https://www.httpbin.org/delay/5"
#     url = "https://www.baidu.com"
#     print('waiting for ',url)
#     resp = await get(url)
#     print('get response from ',url)
#
# tasks = [asyncio.ensure_future((request())) for _ in range(5)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# end_time = time.time()
# print('total time: ',end_time-start_time)

#测试百度
def test(num):
    start_time = time.time()
    async def get(url):
        session = aiohttp.ClientSession()
        resp = await session.get(url)
        await resp.text()
        await session.close()
        return resp
    async def request():
        url = "https://www.baidu.com"
        # print('waiting for ',url)
        resp = await get(url)
        # print('get response from ',url)

    tasks = [asyncio.ensure_future((request())) for _ in range(num)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end_time = time.time()
    print('num,total time: ',num,end_time-start_time)




if __name__ == '__main__':
    for num in [1, 10, 50, 200, 500]:
        test(num)