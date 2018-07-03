from pythonds.basic.stack import Stack
from timeit import Timer

class Queue1:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Queue2:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
q1=Queue1()
q1.enqueue(4)
q1.enqueue('dog')


q2=Queue2()
q2.enqueue(4)
q2.enqueue('dog')



t1=Timer('q1.enqueue(True)','from __main__ import q1')
print('for queue 1 ',t1.timeit(number=1000),'milliseconds')

t2=Timer('q2.enqueue(True)','from __main__ import q2')
print('for queue 2 ',t2.timeit(number=1000),'milliseconds')
