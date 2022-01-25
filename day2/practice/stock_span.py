def calculate_span(prices):
    '''
    Function to calculate the span of a given stock, given its stock prices on different days
    '''
    # length of prices list
    n = len(prices)

    # array to store span 
    S = [None]*n

    # intialize an empty stack 
    st = []
    # append the first element in the stack 
    st.append(0)

    # first element's span is always 1 
    S[0] = 1

    # traverse left from each element as long as we don't find an element greater than the current element
    for i in range(1, n):

        # if the top of the stack is smaller than or equal to prices[i], then that element pops from the stack 
        while(len(st) > 0 and prices[st[-1]] <= prices[i]):
            # pop from stack 
            st.pop()
        # print(len(st))

        # update span value for ith element - i+1 if the stack is empty (which means all elements to the left are smaller)
        # i - index at the top of the stack if the stack is not empty 
        S[i] = i + 1 if len(st) <= 0 else i - st[-1]
            
        # push the current value to the stack 
        st.append(i)

    return S

# prices
prices = [100, 80, 60, 70, 60, 75, 85]
print('Span values for the given stock are: '.format(calculate_span(prices)))





