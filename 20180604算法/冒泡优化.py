
def bubble_sort(items, comp=None):
    """冒泡排序"""

    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            result = items[j] > items[j + 1] if not comp else \
                comp(items[j], items[j + 1]) > 0
            if result:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, 0, -1):
                result = items[j] < items[j-1] if not comp else\
                    comp(items[j], items[j - 1]) < 0
                if result:
                    items[j], items[j - 1] = \
                       items[j - 1], items[j]
        if not swapped:
            break


class Student(object):
    """学生类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}:{self.age}'


def main():
    """主函数"""
    items = [23, 12, 45, 11, 56, 9, 89]
    bubble_sort(items)
    print(items)
    items2 = [
        Student('Wang Dachui', 25),
        Student('Luo Hao', 38),
        Student('Zhang Sanfeng', 120),
        Student('Bai yuanfang', 18)
    ]
    bubble_sort(items2, lambda s1, s2: s1.age - s2.age)
    print(items2)
    items3 = ['apple', 'watermelon', 'pitaya', 'waxberry', 'pear']
    bubble_sort(items3, lambda s1, s2: len(s1) - len(s2))
    print(items3)


if __name__ == '__main__':
    main()
