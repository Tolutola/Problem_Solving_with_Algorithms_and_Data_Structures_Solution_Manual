# Write a program that solves the following problem: Three missionaries and three cannibals come to a river and find a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of crossings that will get everyone safely to the other side of the river.


def printStatus(start,target,mvChoice,forwardFlag):
    print('\n')
    if forwardFlag:
        print('moving {} missionaries and {} cannibals to destination...'.format(mvChoice[0],mvChoice[1]))
    else:
        print('moving {} missionaries and {} cannibals back to starting point...'.format(mvChoice[0],mvChoice[1]))

    print('{} missonaries and {} cannibals at the starting point and {} missonaries and {} cannibals destination'.format(start[0],start[1],target[0],target[1]))


def crossings(start,target):
    # each choice is a list of two numbers:
    # first is represents how many missionaries moved, second how many cannibals moved
    backChoices=[[1,1],[1,0],[0,1]]
    forwardChoices=[[2,0],[0,2],[1,1]]

    n_counter=0
    while sum(target)!=6 and n_counter<10: # we still have some trips to make

        # backward trip
        b=2
        continueFlag=True
        while (b>=0) & continueFlag:

            choice=backChoices[b]
            temp_start=[start[i]+choice[i] for i in range(2)]
            temp_target=[target[i]-choice[i] for i in range(2)]


            # check that start and destination numbers are not less than zero
            start_pos=all([x>=0 for x in temp_start])
            target_pos=all([x>=0 for x in temp_target])


            if (((temp_start[0]>=temp_start[1])  or temp_start[0]==0) & ((temp_target[0]>=temp_target[1]) or temp_target[0]==0) & (start_pos) & (target_pos)):
                # move is possible
                start=temp_start
                target=temp_target

                printStatus(start,target,choice,False)

                continueFlag=False
                break
            b-=1

        # forward trip
        f=0
        continueFlag=True
        while (f<3) and continueFlag:
            choice=forwardChoices[f]
            temp_start=[start[i]-choice[i] for i in range(2)]
            temp_target=[target[i]+choice[i] for i in range(2)]

            # check that start and destination numbers are not less than zero
            start_pos=all([x>=0 for x in temp_start])
            target_pos=all([x>=0 for x in temp_target])



            if (((temp_start[0]>=temp_start[1]) or temp_start[0]==0) & ((temp_target[0]>=temp_target[1]) or temp_target[0]==0) & (start_pos) & (target_pos)):
                # move is possible
                start=temp_start
                target=temp_target

                printStatus(start,target,choice,True)

                continueFlag=False
                break
            f+=1

        n_counter+=1



nM=3 # number of missionaries
nC=3 # number of cannibals

# start and target are lists with the number of missionaries and cannibals
start=[nM,nC]
target=[0,0]

crossings(start, target)
