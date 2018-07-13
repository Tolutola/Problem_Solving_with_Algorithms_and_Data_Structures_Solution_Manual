def pascal(nrows):
    printList=[]

    for i in range(nrows):
        printList.append([])
        printList[i].append(1)
        for j in range(1,i):
            printList[i].append(printList[i-1][j-1]+ printList[i-1][j])

        if (i!=0):
            printList[i].append(1)

    for i,plist in enumerate(printList):
        print(' '*(nrows-i) + ' '.join([str(x)+' ' for x in plist]))

pascal(5)
