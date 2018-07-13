
#gallery  is a list of tuples  [item, weight, value]
def art_thief(gallery,wt_limit,sack):
    current_values=[item[2] for item in gallery]
    to_steal=current_values.index(max(current_values))
    sack.append(gallery.pop(to_steal))
    if sum([item[1] for item in sack])>wt_limit: # nope you can't steal that
        sack.pop()
        value=0
        wt=0
        print('Items stolen')
        for item in sack:
            print('Item {}: weight: {}  value: {}'.format(item[0],item[1],item[2]))
            wt+=item[1]
            value+=item[2]
        print('\ntotal weight: {}  total value: {}'.format(wt,value))

        return

    else:
        art_thief(gallery,wt_limit,sack)

gallery=[(1,2,3),(2,3,4),(3,4,8),(4,5,8),(5,9,10)]

wt_limit=20
sack=[]

art_thief(gallery,wt_limit,sack)
