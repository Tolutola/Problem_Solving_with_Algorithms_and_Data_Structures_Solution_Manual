

from pythonds.basic.stack import Stack


def moveTower(height,fromPole,toPole,withPole,StackDict):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole,StackDict)
        moveDisk(fromPole,toPole,StackDict)
        moveTower(height-1,withPole,toPole,fromPole,StackDict)

def moveDisk(fp,tp,StackDict):
    movedDisk=StackDict[fp].pop()
    StackDict[tp].push(movedDisk)
    print("moving disk {} from {}  to {}".format(movedDisk,fp,tp))


my_stacks={'A':Stack(),'B':Stack(),'C':Stack()}

#move from A to B using C
height=3
for i in range(height):
    my_stacks['A'].push(height-i)
moveTower(height,'A','B','C',my_stacks)
