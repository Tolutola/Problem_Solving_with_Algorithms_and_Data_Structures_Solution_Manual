
def water(big_jug_size,small_jug_size,water_amt):
    big_w=0 # water in big jug
    small_w=0 # water in small jug

    while not(water_amt in [small_w,big_w]):
        # if the big jug is empty, fill it
        if big_w==0:
            big_w=big_jug_size
        # if the small jug is full, empty it
        if small_w==small_jug_size:
            small_w=0;

        # transfer water from big jug to small jug
        water_excess=big_w-(small_jug_size-small_w)

        if water_excess>=0:
            small_w= small_jug_size
            big_w=water_excess
        else:
            small_w+=big_w
            big_w=0

    #move the water to the right jug if necessary
    if water_amt!=big_w:
        big_w=small_w
        small_w=0

    print ('amount in small jug: {}; \namount in big jug: {}'.format(small_w,big_w))


water(5,4,2)
# water(5,3,1)
