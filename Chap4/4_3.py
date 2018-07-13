

# Modify the branchLen recursively so that instead of always subtracting the same amount you
#  subtract a random amount in some range.

import turtle
from numpy.random import randint

def tree(branchLen,t,p,a,l):

    if p<0:
        p=0.1


    if p>=1.5:
        sub_c='brown'

    else:
        sub_c='green'

    #branch thickness
    t.pensize(p)

    #leaf angle
    sub_a=randint(15,45)

    #

    sub_l=randint(5,15) # decrement length


    if branchLen > 5:

        t.color(sub_c)
        t.forward(branchLen)

        t.right(a) # 20
        tree(branchLen-l,t,p-0.5,sub_a,sub_l)
        #branch color
        t.color(sub_c)

        t.left(2*a)
        tree(branchLen-l,t,p-0.5,sub_a,sub_l)
        #branch color
        t.color(sub_c)

        t.right(a)

        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    t.pensize(3)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    angle=randint(15,45)
    pensize=3
    length=randint(15,45) # original decrement length
    tree(75,t,pensize,angle,length)
    myWin.exitonclick()

main()
