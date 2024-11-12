import time

# def func():
#     print("hello")
#     time.sleep(3) #让当前的线程处于阻塞状态，3秒后恢复CPU是不工作的
#     print("world")
#
# if __name__ == '__main__':
#     func()


#input() 程序也是处于阻塞状态

#requests.get(bilibili) 在网络请求返回数据之前，程序处于阻塞状态
#一般情况下，程序处于IO操作的时候，都会处于阻塞状态

#协程： 当程序遇见IO操作的时候，可以选择性的切换到其他任务上，而不是阻塞在IO操作上。


#在微观上是一个任务一个任务的进行切换，切换条件一般是IO操作
#在宏观上我们看到的其他事多个任务一起在进行
#多任务异步操作

#上面所讲的是单线程的条件下

import asyncio

from win32comext.shell.demos.servers.folder_view import tasks


# 协程的实现
# async def func():
#     print("你好")

# if __name__ == '__main__':
#     g = func() #此时的函数是异步携程函数，此时函数执行得到的是一个携程对象
#     # print(g)
#     asyncio.run(g) #x=携程程序允许需要asyncio模块的支持


# async def func1():
#     print("奥特曼")
#     # time.sleep(2)
#     await  asyncio.sleep(3) #异常操作的代码
#     print("奥特曼")
#
# async def func2():
#     print("奥特曼2222222222")
#     await  asyncio.sleep(2)
#     print("奥特曼222222222")
#
# async def func3():
#     print("奥特曼33333333")
#     await  asyncio.sleep(4)
#     print("奥特曼33333333")
#
#
# if __name__ == '__main__':
#     g1 = func1()
#     g2 = func2()
#     g3 = func3()
#     tasks = [g1, g2, g3]
#     t1 = time.time()
#     # 手动创建和管理事件循环
#     loop = asyncio.get_event_loop()
#     try:
#         loop.run_until_complete(asyncio.gather(*tasks))
#     finally:
#         loop.close()
#
#     t2 = time.time()
#     print(f"总耗时: {t2 - t1} 秒")
#     print("程序结束")

#
# async def func1():
#     print("奥特曼")
#     # time.sleep(2)
#     await  asyncio.sleep(3) #异常操作的代码
#     print("奥特曼")
#
# async def func2():
#     print("奥特曼2222222222")
#     await  asyncio.sleep(2)
#     print("奥特曼222222222")
#
# async def func3():
#     print("奥特曼33333333")
#     await  asyncio.sleep(4)
#     print("奥特曼33333333")
#
#
# async def main():
#     #第一种写法
#     # f1 = func1()
#     # await f1 #一般await挂起操作放在协程对象前面
#     # f2 = func2()
#     # await f2
#     # f3 = func3()
#     # await f3
#
#     #第二种写法(推荐)
#     tasks=[func1(), func2(), func3()]
#
#     await asyncio.gather(*tasks)  # 使用gather而不是wait
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(f"总耗时: {t2 - t1} 秒")

#在爬虫领域，使用asyncio可以做到多线程，多进程，多协程

async def download_one_page(url):
    print(f"开始下载: {url}\n")
    await asyncio.sleep(2)  # 模拟网络请求
    print(f"下载完成: {url}\n")

async def main():
    urls = [
        "www.baidu.com"
        "www.bilibili.com"
        "www.sogou.com"
    ]
    tasks=[]

    for url in urls:
        task = download_one_page(url)
        tasks.append(task)

    # 使用 asyncio.gather 并发执行所有任务
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())

