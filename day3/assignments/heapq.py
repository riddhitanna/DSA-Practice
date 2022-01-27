'''
Day 3 - Heaps and hash table
Date: 27-Jan-2022
'''

import heapq as heap
from time import time


def min_avg_wait(cust_time):
    '''
    Function to calculate the minimum avergae waiting time given the customer arrival time and the time taken to cook
    their order 

    Follows the Shortest Job First scheduling (SJF) using heap data structure in Python
    '''
    # number of customers
    n = len(cust_time)

    # tot_time keeps track of time elapsed, wait_time keeps track of the sum of waiting time for each of the customers
    tot_time = wait_time = 0

    # keep track of which customer has arrived and is in queue at the moment - at time t
    queue = []

    # sorting the arrival time in descending order - so that it is efficient to pop (from end)
    cust_time.sort(reverse=True)

    # loop while customers are yet to arrive or are in queue
    while cust_time or queue:
        while cust_time and cust_time[-1][0] < tot_time:
            # push the customer that arrives at this time step into the queue
            heap.heappush(queue, (cust_time.pop()[::-1]))

        # if there are customers in queue, then pop the customer whose cooking time is the least for SJF
        if queue:
            cook = heap.heappop(queue)

            # to the total time, add the time taken to cook for this customer
            tot_time += cook[0]

            # update the wait time for this customer and add it to waiting time
            # waiting time for a customer = total time elapsed - arrival time of customer
            wait_time += tot_time - cook[1]

        # if queue is empty, push the first customer into the queue
        else:
            heap.heappush(queue, cust_time.pop()[::-1])

            # arrival time of the first customer is the time elapsed till now
            tot_time = queue[0][1]

    return wait_time // n


# to store the arrival time and cooking time for each of the customers
cust_time = []

# number of customers
N = int(input('Enter the number of customers: '))
for i in range(N):
    t, l = map(int, list(input(
        'Enter the arrival time and cooking time for customer {}: '.format(i+1)).split()))
    cust_time.append([t, l])

print(min_avg_wait(cust_time))
