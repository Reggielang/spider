# 线程,进程
# 进程是资源单位,每一个进程至少有一个线程,线程是CPU调度的最小单位
# 线程是执行单位

# 多线程
from threading import Thread

def func(name):
    for i in range(1000):
        print(name,i)


if __name__ == '__main__':
    t1 = Thread(target=func,args=("王力宏",)) #创建线程,并给线程安排任务
    # 多线程状态可以开始工作状态,具体的执行时间有CPU决定
    t1.start()
    t2 = Thread(target=func,args=("周杰伦",)) #创建线程,并给线程安排任务
    # 多线程状态可以开始工作状态,具体的执行时间有CPU决定
    t2.start()
    for i in range(1000):
        print("main",i)


# class MyThread(Thread):
#     def run(self): # 重写run方法
#         for i in range(1000):
#             print(i)
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start() # 开始执行
#
#     for i in range(5):
#         print("main",i)