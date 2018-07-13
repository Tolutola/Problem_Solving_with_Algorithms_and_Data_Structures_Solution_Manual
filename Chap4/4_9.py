
def water(big_jug_size,small_jug_size,water_amt):
    big_w=0 # water in big jug
    small_w=0 # water in small jug

    # while small_w != abs(small_jug_size-water_amt ):
    # fill big jug
    big_w+=big_jug_size
    # transfer water from big jug to small jug
    water_transfered=small_jug_size-small_w
    small_w+=water_transfered
    big_w-=water_transfered

    # empty small jug and transfer water from big jug to small jug
    small_w=big_w
    big_w=0

    #fill big jug and then use it to fill up the small jug
    big_w= big_jug_size-(small_jug_size-small_w)
    small_w=small_jug_size

    print ('amount in small jug: {}; \namount in big jug: {}'.format(small_w,big_w))



water(4,3,2)
