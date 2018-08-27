
# 二分查找 序列必须有序


def binary_search(mylist, item):

    start = 0
    end = len(mylist)-1

    while start <= end:
        mid = (start+end) // 2
        guess = mylist[mid]
        if guess > item:
            end = mid - 1
        elif guess < item:
            start = mid + 1
        else:
            return mid
    return -1


ml = [1, 3, 5, 7, 9]
print(binary_search(ml, 3))

