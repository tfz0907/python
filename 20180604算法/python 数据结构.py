# 实现队列

# class Queue():
#     def __init__(self):
#         self.items=[]
#
#     def enqueue(self,item):
#         # 入队 O(1)
#         self.items.append(item)
#
#     def dequeue(self):
#         # 出队 O(n)
#         return self.items.pop(0)
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return self.size()==0
#
#
# q_list=Queue()
# q_list.enqueue(1)
# q_list.enqueue(2)
# q_list.enqueue(4)
# print(q_list.dequeue())
# print(q_list.dequeue())
# print(q_list.dequeue())
# print(q_list.dequeue())

# 第二种创建队列方法 O(1)
from collections import deque

# class Queue2():
#     def __init__(self):
#         self.items=deque()
#     def enqueue(self,item):
#         self.items.append(item)
#     def dequeue(self):
#         return self.items.popleft()
#     def size(self):
#         return len(self.items)
#     def is_empty(self):
#         return self.size()==0
# q_list=Queue2()
# q_list.enqueue(1)
# q_list.enqueue(2)
# q_list.enqueue(4)
# print(q_list.dequeue())
# print(q_list.dequeue())
# print(q_list.dequeue())
# print(q_list.dequeue())



# 双端队列
# deque 方法队首弹出复杂度为 O(1)
# from collections import deque
#
# class Deque():
#     def __init__(self):
#         self.items = deque()
#
#     def addFront(self,item):
#         self.items.appendleft(item)
#     def addRear(self,item):
#         self.items.appendleft(item)
#
#     def removeFront(self):
#         return self.items.popleft()
#     def removeRear(self):
#         return self.items.pop()
#     def size(self):
#         return len(self.items)
#     def is_empty(self):
#         return self.size() == 0


# 用双端队列验证字符串回文
# 字符串回文就是正反读都一样 abba

#
# def palchecker(str):
#     two_queue = Deque()
#     for i in str:
#         two_queue.addRear(i)
#     while two_queue.size() > 1:  # 防止奇数长的字符串
#         first = two_queue.removeFront()
#         print(first)
#         last = two_queue.removeRear()
#         print(last)
#         if first != last:
#             return False
#     return True
# str='level'
# #print(palchecker(str))
# palchecker(str)

# 表结点类
# class Node():
#     def __init__(self, elem):
#         self.data = elem
#         self.next = None
#     def getData(self): # 获取数据域
#         return self.data
#     def getNext(self): # 获取链接域
#         return self.next
#     def setData(self,newData): # 设置数据域
#         self.data = newData
#     def setNext(self,newAddr): # 设置链接域
#         self.next = newAddr

# print(id(Node))  # 117446544
# print(id(Node(0)))  # 61376144
# print(id(Node(0).__init__(0)))  # 1400663560
# print(id(Node(0).data))  # 1400784512
# print(id(Node(0).next))  # 1400663560
# print(id(Node(0).getNext()))  # 1400663560
# print(id(Node(0).getData()))  # 1400784512
# print(id(Node(0).setData(1)))  # 1400663560
# print(id(Node(0).setNext('s')))  # 1400663560
# print(Node(0).data)
# print(Node(0).__init__(0)) # 干扰 None

# 循环链表
# class SinCycLinkedList():
#     def __init__(self):
#         self.Lnode = Node(None) # 创建一个结点
#         self.Lnode.setNext(self.Lnode) # 循环链表
#     def add(self,item):
#         temp = Node(item) # 添加新节点
#         temp.setNext(self.Lnode.getNext())  # 将新节点的链接域指向旧节点
#         self.Lnode.setNext(temp) # 将旧节点的链接域指向新节点
#     def remove(self,item):
#         prev = self.Lnode
#         while prev.getNext() != self.Lnode:
#             cur = prev.getNext()
#             if cur.getData() == item:
#                 prev.setNext(cur.getNext())
#             prev = prev.getNext()
#
#
#     def is_empty(self):
#         return self.Lnode.getNext() == self.Lnode
#     def size(self):
#         count = 0
#         cur = self.Lnode.getNext()
#         while cur != self.Lnode:
#             count += 1
#             cur = cur.getNext()
#         return count
#
#
#
# myL=SinCycLinkedList()
# # print(myL.size())
# # print(myL.is_empty())
# myL.add(3)
# myL.add('r')
# myL.add('t')
# #print(myL.size())
# # print(myL.is_empty())
# # myL.remove('r')
# # print(myL.size())
"""
抽象一个链表：
ADT List:
    List(self)
    is_empty(self)
    len(self)
    prepend(self,elem)
    append(self,elem)
    insert(self,elem,i)
    del_first(self)
    del_last(self)
    del(self,i)
    search(self,elem)
    forall(self,op)

"""
"""
实现一个线性表需要的条件：
1. 能直接或间接的找到表中首元素
2. 从表中任一元素出发，能找到它之后的下一元素
线性表有两种存储方式： a.顺序表（将元素保存在连续的存储区） b.链表
  链表的实现方式如下：
    1.把表中的元素分别存储在一批独立的存储块（称为表结点）里
    2.保重从组成表结构中的任一个结点可以找到与其相关的下一个结点
    3.在前一结点里用链接的方式显示的记录与下一结点之间的联系

"""


# 定义一个简单表结点

class LNone(object):
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_


# 单链表

class LinkedList(object):
    def __init__(self):
        # 头指针
        self.head = None
        # 尾指针
        self.tail = None

    def remove(self, index):
        cur = self.head
        cur_index = 0
        if self.head is None:  # 空链表
            raise Exception('The list is an empty list')
        while cur_index < (index - 1):
            cur = cur.next_
            if cur is None:
                raise Exception('List length less than index')
            cur_index += 1
        if index == 0:
            self.head = cur.next_
            #cur = cur.next_
            return
        if self.head is self.tail:  # 当只有一个结点
            self.head = None
            self.tail = None
            return
        cur.next_ = cur.next_.next_
        if cur.next_ is None:
            self.tail = cur

    # 测试链表是否为空
    def is_empty(self):
        return self.head is None

    def prepend(self):
        pass

    def append(self, data):
        # 每添加一个结点就实例化一个结点类
        node = LNone(data)
        if self.head is None:  # 链表为空
            self.head = node  # 将头指针指向当前结点
            self.tail = node  # 将尾指针指向当前结点
        else:
            # 把上一个结点的尾指针指向当前结点
            self.tail.next_ = node
            self.tail = node  # 将链表尾指针指向当前结点

    def insert(self, index, value):
        cur = self.head
        cur_index = 0
        if cur is None:
            raise Exception('The list is an empty list')
        # 查找插入位置的前一个结点信息（指针域）
        while cur_index < (index - 1):
            cur = cur.next_
            if cur is None:
                raise Exception('List length less than index')
            cur_index += 1
        node = LNone(value)
        # 1将原结点的指针域赋给新节点的指针域
        node.next_ = cur.next_
        # 2将指向新节点的引用赋给原结点的指针域
        cur.next_ = node
        if node.next_ is None:
            self.tail = node

    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next_:
            cur = cur.next_
            yield cur.data

    def size(self):
        current = self.head
        count = 0
        if current is None:
            raise Exception('The list is an empty list')
        while current is not None:
            count += 1
            current = current.next_
        return count

    # 查找是否有这个值
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next_
        return found


ll = LinkedList()
ll.append(5)
ll.append(7)
ll.append('r')
ll.append('rd')
# ll.insert(4,8)
# print(list(ll.iter()))
ll.remove(0)
print(list(ll.iter()))
# print(ll.size())
# print(ll.search('r'))


# print(ll.is_empty())
# print(ll.head.data)
# print(ll.tail.data)
# print(ll.head.next_.next_.data) # 头结点的下下个结点数据
# print(ll.tail.next_)


##################               栈               #############################
# 用内置方法实现
# 实现栈(实例用于十进制转二进制)
# class Stack():
#
#     def __init__(self):
#         self.items = []
#       # 先进
#     def push(self,item):
#         self.items.append(item)
#        # 后出
#     def pop(self):
#         return self.items.pop()
#     def size(self):
#         return len(self.items)
#     #栈顶
#     def top(self):
#         return self.items[self.size()-1]
#     def clear(self):
#         del self.items[:]
# s_stack=Stack()
# s_stack.push(1)
# s_stack.push(2)
# s_stack.push(4)
# print(s_stack.pop())
# print(s_stack.pop())
# print(s_stack.pop())

# 不用内置方法实现

# class Node(object):
#
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Stack(object):
#     def __init__(self):
#         self.top = None
#
#     # 压栈
#
#     def push(self, value):
#         node = Node(value)
#         node.next = self.top
#         self.top = node
#
#     # 抛出栈顶数据，栈顶数据变化
#
#     def pop(self):
#         # 临时变量 head 指向栈顶
#         head = self.top
#         if head is None:
#             raise Exception('This is en empty stack')
#         self.top = head.next
#         return head.value
#
#     # 返回栈顶数据，但不删除
#
#     def peek(self):
#         head = self.top
#         if head is None:
#             raise Exception('This is en empty stack')
#         return head.value
#
#     # 判断是否空栈
#
#     def is_empty(self):
#         return not self.top
#
#     def size(self):
#         head = self.top
#         count = 0
#         if head is Node:
#             raise Exception('This is en empty stack')
#         while head is not None:
#             count += 1
#             head = head.next
#         return count
#


""" 哈希表 """

# 存放在链表中的元素类
class Node(object):

    def __init__(self,key,value):
        self.key = key
        self.value = value

class Map(object):
    def __init__(self, init_size, hash = hash):
        self.__slots = [[] for _ in range(init_size)]
        self.__size = init_size
        self.hash = hash

    def put(self, key, value):
        node = Node(key,value)
        address = self.hash(node.key) % self.__size
        self.__slots[address].append(node)

    def get(self,key, default = None):
        _key = self.hash(key)
        address = _key % self.__size
        for node in self.__slots[address]:
            if node.key == key:
                return node.value
        return default
    def remove(self,key):
        address = self.hash(key) % self.__size
        for index,node in enumerate(self.__slots[address].copy()):
            if node.key == key:
                self.__slots[address].pop(index)
