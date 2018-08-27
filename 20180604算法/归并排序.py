
# def merge_sort(seq):
#     if len(seq) <= 1:
#         return seq
#     mid = len(seq) // 2
#     left = merge_sort(seq[:mid])
#     right = merge_sort(seq[mid:])
#     return merge(left, right)
#
#
# # 传入两个有序列表
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
#
# l = [2, 33, 12 ,43, 1, 7]
# merge_sort(l)
# print(l)


def merge(left, right, comp=lambda x, y: x <= y):
    items = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if comp(left[li], right[ri]):
            items.append(left[li])
            li += 1
        else:
            items.append(right[ri])
            ri += 1

    items += left[li:]
    items += right[ri]
    return items


def merge_sort(items, comp=lambda x, y: x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)














