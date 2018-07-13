def reverseList(mylist):
    if len(mylist)==1:
        return [mylist[0]]
    else:
        return  [mylist[-1]] + reverseList(mylist[:-1])
