# import turtle
#
# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()
#
# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)
#
# drawSpiral(myTurtle,100)
# myWin.exitonclick()

# Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
# Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
# Modify the angle used in turning the turtle so that at each branch point the angle is selected at
#  random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
# Modify the branchLen recursively so that instead of always subtracting the same amount you
#  subtract a random amount in some range.

import turtle
from numpy.random import randint

def tree(branchLen,t,p,a):
    t.pensize(p)
    sub_a=randint(15,45)
    if branchLen > 5:
        t.forward(branchLen)

        t.right(a) # 20
        tree(branchLen-15,t,p-0.5,sub_a)
        t.left(2*a)
        tree(branchLen-15,t,p-0.5,sub_a)
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
    t.color("green")
    angle=randint(15,45)
    pensize=3
    tree(75,t,pensize,angle)
    myWin.exitonclick()

main()
