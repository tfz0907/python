from functools import wraps


# def outer(func):
#     @wraps(func)
#     def inner():
#         print('调用func前')
#         ret = func()
#         print('调用func后')
#         return ret
#     return inner
#
#
# @outer
# def myfunc():
#     print('我是被装饰函数')
#     return '被装饰函数返回值'
#
#
# a=myfunc()
# print(a)