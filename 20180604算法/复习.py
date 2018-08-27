# 变量作用域 搜索顺序：legb
"""时间和空间是不可掉和的矛盾
    软件和硬件逻辑上是等效的
"""
"""
Git 服务器（版本控制）
代码托管（Github,Gitee,CONDING)
私服：GitLab

# 克隆项目
git clone url [rename,]

# (将修改纳入暂存区)
git add .
. 表示所有
也可以这样 git add filename
# 查看暂存区状态
git status (查看状态)

git checkout -- filename

# 提交（在本地实施版本控制）
git commit -m '修改原因'

# 上传到托管平台
git push
# 更新下载
git pull

# 查看日志
git log
# 查看日志（包括未来本本）
git reflog

# 回到历史版本
git reset --hard HEAD^

HEAD^ 表示上一个版本
HEAD^^ 表示上上一个版本
 --hard 后也可以加版本的哈希码

"""
""" 函数调用需要保存执行现场和恢复执行现场（靠栈实现）
 栈空间很小 ，所以不能不加节制的使用，如果递归不能迅速收敛，那么就有可能导致栈溢出
"""


"""
走台阶

"""


def walk(n, temp={}):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    try:
        return temp[n]
    except KeyError:
        temp[n] = walk(n-1) + walk(n-2) + walk(n-3)
        return temp[n]


def fib2(n: int, temp={}):
    if n == 1 or n == 2:
        return 1
    try:
        return temp[n]
    except KeyError:
        temp[n] = fib2(n-1) + fib2(n-2)
        return temp[n]


# 穷举法 动态规划  贪婪 分治

def search(items, key):
    """顺序查找(时间复杂度为 O(n))"""
    for i in range(len(items)):
        if items[i] == key:
            return i


my_list = [12, 3, 24, 454, 8]
print(search(my_list, 8))


def binary_search(items, key):
    """二分查找"""
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = (start + end) // 2  # 从中间开始猜
        guess = items[mid]
        if guess > key:  # 猜大了
            end = mid - 1  # 结束位变为中间值-1
        elif guess < key:  # 猜小了
            start = mid + 1  # 起始位=中间值+1
        else:
            return mid
    return -1


ml = [1, 3, 5, 7, 9]
# print(binary_search(ml, 3))

"""五个人去捕鱼 第二天早上 第一个人醒来 将鱼分成五份 把多余的一条鱼扔掉 拿走一份 
第二个醒来 也将鱼分成5份 把多余的一条鱼扔掉 拿走一份
 另外三个人依次醒来 也按同样的方法拿走鱼 问他们至少捕了多少鱼?"""


def enumeration(n):
   pass