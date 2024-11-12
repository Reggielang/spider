# 线程,进程
# 进程是资源单位,每一个进程至少有一个线程,线程是CPU调度的最小单位
# 线程是执行单位

#多进程
from multiprocessing import Process

def func():
    for i in range(1000):
        print("子进程",i)


if __name__ == '__main__':
    p  = Process(target=func)
    p.start()
    for i in range(1000):
        print("主进程",i)