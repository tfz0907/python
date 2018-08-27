# 1 使用装饰器
# from functools import wraps
# def Singleton(cls):
#     _instance = {}
#     @wraps(cls)
#     def singleton(*args,**kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args,**kwargs)
#         return _instance[cls]
#
#     return singleton
#
# @Singleton
# class A(object):
#     a = 1
#     def __init__(self,x=None):
#         self.x = x
#
# a1 = A(2232323232323)
# a2 = A('a_b')
# print(id(a1))  # 20874640
# print(id(a2))  # 20874640
#

# 使用类
# 不支持多线程
# class Singleton(object):
#
#     def __init__(self):
#         time.sleep(1) # 模拟io操作
#     @classmethod
#     def instance(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             Singleton._instance = Singleton(*args,**kwargs)
#         return Singleton._instance


# a1 = Singleton.instance()  # 单例
# a2 = Singleton.instance()
# a3 = Singleton()  # 非单例
# print(id(a1))
# print(id(a2))
# 测试上述方法是否支持多线程
import threading
import time

# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()



# 支持多线程单例
# class Singleton(object):
#     # 加锁
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         time.sleep(1) # 模拟IO操作
#     @classmethod
#     def instance(cls,*args,**kwargs):
#         if not hasattr(Singleton,'_instance'):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton,'_instance'):
#                     Singleton._instance = Singleton(*args,**kwargs)
#         return Singleton._instance
#
# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
#
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()


# 使用__new__

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

def task():
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task)
    t.start()























