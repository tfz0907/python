#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tfz


def bubble_sort(args_list):
    args_list_length = len(args_list)  # 获取列表长度
    swapped = False
    for i in range(args_list_length - 1):  # 需要比较 n-1 次

        for j in range(0, args_list_length - 1 - i):
            if args_list[j] > args_list[j + 1]:  # 第j趟比较
                args_list[j], args_list[j + 1] = args_list[j + 1], args_list[j]
                swapped = True  # swapped = True 说明进行了交换

        if swapped:
            swapped = False
            for j in range(args_list_length - 2 - i, 0, -1):
                if args_list[j] < args_list[j - 1]:
                    args_list[j], args_list[j - 1] = args_list[j - 1], args_list[j]
                    swapped = True
        if not swapped:
                break



if __name__ == '__main__':
    mylist = [12, 34, 4, 12, 5, 2, 9, 4, 123, 33, 54]
    print("原列表为：{}".format(mylist))
    bubble_sort(mylist)
    print("新列表为：{}".format(mylist))
