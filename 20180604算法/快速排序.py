def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # 基准值
        # print(pivot)
        left = [i for i in array[1:] if i <= pivot]  # 小于基准值放一个列表
        # print(left)
        right = [i for i in array[1:] if i > pivot]  # 大于基准值放另一个列表
        return quick_sort(left) + [pivot] + quick_sort(right)  # 递归调用


# print(quick_sort([23,4,5,1,78,12]))

qs = lambda xs: \
((len(xs) <= 1 and [xs]) or [qs([x for x in xs[1:] if x < xs[0]]) + [xs[0]] + qs([x for x in xs[1:] if x >= xs[0]])])[0]

print(qs([23, 4, 5, 1, 78, 12]))
