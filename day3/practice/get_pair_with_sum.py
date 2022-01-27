def get_pair_with_sum(numbers, sum):

    # define an empty dictionary - it will store all the elements that we have already traversed
    d = {}

    # enumerate through all the numbers to see if a pair with given sum exists
    for i,e in enumerate(numbers):
        #print(i, e)
        if sum - e in d:
            print('Pair with sum {} is ({}, {})'.format(sum, e, sum-e))
            return
        d[e] = i
    print('Pair not found')    
    




numbers = [1, 2, 4, 5]
sum = int(input('Enter the sum to find: '))

get_pair_with_sum(numbers, sum)