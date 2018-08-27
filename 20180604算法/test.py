"""测试"""
# c1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
# c2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]

# for i in c2:
#     a=[val for val in c1 if val in i]
#     print(a)

# c = [list(filter(lambda x:x in c1, sublist)) for sublist in c2]
# print(c)

# import json
#
# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
# print(data)
# json_str = json.dumps(data)
# print(json_str)
# data1 = json.loads(json_str)
# print(type(data1))


def bubble_sort(args):
    """冒泡排序"""
    list_len = len(args)
    for i in range(0, list_len - 1):
        for j in range(0, list_len - i - 1):
            if args[j] > args[j + 1]:  # 第J 趟比较
                args[j], args[j + 1] = args[j + 1], args[j]


def merge(left, right):
    """合并两个有序列表"""
    items = []
    idx1, idx2 = 0, 0
    while idx1 < len(left) and idx2 < len(right):
        if left[idx1] < right[idx2]:
            items.append(left[idx1])
            idx1 += 1
        else:
            items.append(right[idx2])
            idx2 += 1
    items += left[idx1:]
    items += right[idx2:]
    return items


def merge_sort(items):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    print(left)
    return merge(left, right)



def main():
    """主函数"""
    my_list = [2, 3, 1, 89, 5, 34, 4]
    bubble_sort(my_list)
    # print(my_list)
    merge_sort(my_list)



if __name__ == '__main__':
    main()
