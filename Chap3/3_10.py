from pythonds.basic.queue import Queue
from collections import defaultdict

def radix(number_list):
    main_bin=Queue()
    bin_list=[]
    for i in range(10):
        bin_list.append(Queue())

    #compute max number of digit places
    str_list=[str(x) for x in number_list]
    max_d=max([len(x) for x in str_list])

    #pad the smaller numbers with zeros
    str_list=['0'*(max_d-len(x)) + x if len(x)<max_d else x for x in str_list ]

    #load the main bin
    for x in str_list:
        main_bin.enqueue(x)

    #the sorting process
    for i in range(max_d-1,-1,-1):
        # remove from main bin and place in the corresponding digit bin
        while main_bin.size()>0:
            temp_digit=main_bin.dequeue()
            bin_list[int(temp_digit[i])].enqueue(temp_digit)

        # return all numbers to the main bin
        for temp_bin in bin_list:
            while temp_bin.size()>0:
                main_bin.enqueue(temp_bin.dequeue())

    sorted_list=[]
    while main_bin.size()>0:
        sorted_list.append(main_bin.dequeue())

    sorted_list=[int(x) for x in sorted_list]

    return sorted_list

#example
print(radix([543,445,567,980,234,12,7004]))
