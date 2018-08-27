class Myiter(object):
    def __init__(self,n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        return self
    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx+=1
            return val
        else:
            raise StopIteration()

my = Myiter(5)
for i in my:
    print(i)