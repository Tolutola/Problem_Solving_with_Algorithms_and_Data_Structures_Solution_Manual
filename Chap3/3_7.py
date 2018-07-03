from pythonds.basic.stack import Stack
from timeit import Timer

# yes using linked lists

# regular queue implementation
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

#using linked lists
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class Queue2:

    def __init__(self):
        self.head = None
        self.tail=None

    def isEmpty(self):
        return self.head == None

    def dequeue(self):

        if self.head!=None:
            temp=self.head.getNext()
            self.head=temp
            # if temp==None:
            #     self.head=None
            # else:
            #     self.head=temp

        else:
            print('empty queue')


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count



    def enqueue(self,item):
        temp=Node(item)
        if self.head==None:
            self.head = temp

        else:
            current=self.tail
            if current!=None:
                current.setNext(temp)

            else:
                self.head.setNext(temp)

            self.tail=temp

q1=Queue1()
[q1.enqueue(i) for i in range(1000)]

q2=Queue2()
[q2.enqueue(i) for i in range(1000)]


t1=Timer('q1.enqueue(True)','from __main__ import q1')
print('for queue 1 ',t1.timeit(number=int(1e5)),'milliseconds')

t2=Timer('q2.enqueue(True)','from __main__ import q2')
print('for queue 2 ',t2.timeit(number=int(1e5)),'milliseconds')
