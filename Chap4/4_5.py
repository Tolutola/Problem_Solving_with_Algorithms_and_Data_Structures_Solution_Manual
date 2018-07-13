from timeit import Timer

def fib_recursive(n):
    if n <= 2:

        return [1 for i in range(n)]
    else:
        return fib_recursive(n-1) + [sum(fib_recursive(n-1)[-2:])]


def fib_iterative(n):
    res=[]
    for i in range (n):
        if i<2:
            res.append(1)
        else:
            res.append(res[i-1]+res[i-2])
    return res

# print(fib_iterative(8))
# print(fib_recursive(8))

#
t1=Timer('fib_iterative(20)','from __main__ import fib_iterative')
print('for iterative implementation',t1.timeit(10),'milliseconds')

t2=Timer('fib_recursive(20)','from __main__ import fib_recursive')
print('for recursive implementation',t2.timeit(10),'milliseconds')
