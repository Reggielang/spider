# 所有的章节内容(名称和ID)
#https://dushu.baidu.com/api/pc/getDetail?data={"book_id::"4306063500"}
import aiofiles
# 异步的操作
# 章节里的所有内容
#https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}

import requests
import aiohttp
import asyncio
import json
from scipy.fftpack import tilbert


#1. 普通请求访问所有章节的cid和名称
#2. 异步操作：访问下一个URL，下载所有的章节内容

#1. 普通请求访问所有章节的cid和名称
async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks=[]
    for item in dic['data']['novel']['items']: #item对应的章节
        title = item['title']
        cid = item['cid']
        # 准备异步的任务
        tasks.append(aiodownload(cid,book_id,title))
        # print(cid,title)

    await asyncio.gather(*tasks)

#2. 异步操作：访问下一个URL，下载所有的章节内容
async def aiodownload(cid,book_id,title):
    data ={
        "book_id": f'{book_id}',
        "cid": f'{book_id}|{cid}',
        "need_bookinfo": 1
    }

    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async  with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            content = dic['data']['novel']['content']
            async with aiofiles.open('novel/'+title,mode="w",encoding='utf-8') as f:
                await  f.write(content)
            print(title,"下载完成")

if __name__ == '__main__':
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+book_id+'"}'
    asyncio.run(getCatalog(url))













