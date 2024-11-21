# import aiohttp
# import asyncio
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text(), response.status
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html, status = await fetch(session, 'https://cuiqingcai.com')
#         print(f'html:{html[:100]}')
#         print(f'status:{status}')
#
#
# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(main())
#     asyncio.run(main())
import asyncio

import aiohttp

#控制并发量的异步
CONCURRENCY = 5
semaphore = asyncio.Semaphore(CONCURRENCY)
session=None
URL = "https://www.baidu.com"
async  def scrape_api():
    async with semaphore:
        print('scraping',URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.wait(scrape_index_tasks)

if __name__ == '__main__':
    asyncio.run(main())
