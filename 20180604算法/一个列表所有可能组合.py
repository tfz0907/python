# l = [1,2,3,4,5,6,7,8,9,0]
# import itertools
#
# for i in range(0,len(l)+1):
#     print(list(itertools.combinations(l,i)))


import copy


def combine(ml, n):
    ans = []
    one = [0] * n

    def next_(li=0, ni=0):
        if ni == n:
            ans.append(copy.deepcopy(one))
            return
        for lj in range(li, len(ml)):
            one[ni] = ml[lj]

            next_(lj + 1, ni + 1)

    next_()
    return ans


my_list = [5, 2, 8, 4]
# for i in range(0, len(my_list) + 1):
#     print(combine(my_list, i))
print(combine(my_list, 3))
