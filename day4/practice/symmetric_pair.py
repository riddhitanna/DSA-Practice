def find_symmetric_pair(pairs):
    '''
    Function to find symmetric pairs in a given set of pairs of integers 
    '''

    # define an empty set
    s = set()

    # iterate through all pairs
    for (x, y) in pairs:
        # if mirror pair exists, print it
        if (y, x) in s:
            print("{} and {} exist.".format((x,y), (y,x)))
        # add pair to set
        s.add((x, y))
        
        



pairs = [(2,1), (3,5), (4,6), (1,2), (5,3), (6,2)]
find_symmetric_pair(pairs)