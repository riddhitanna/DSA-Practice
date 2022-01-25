'''
Contains implementation of stacks in Python.

Date: 25-Jan-2022

1. To push any element in the stack, call the push() function
2. To delete any element from the stack, call the pop() function
3. To get the maximum element from the stack, call the get_max() function 

'''


class Node:
    '''
    Individual node of a linked list
    '''
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class Stack:
    '''
    Class to implement the functions of a stack
    '''
    def __init__(self):

        # initialize head to none
        self.head = None

    def print_stack(self):
        '''
        Function to print the elements of the linked list
        '''

        # check if linked list is empty
        if self.head == None:
            print("Stack is empty.")
            return

        # iterate through linked list
        itr = self.head
        sstr = ''

        # append all elements to string
        while itr:
            # print(itr.data)
            sstr = sstr + str(itr.data) + '->'
            itr = itr.nxt

        # print the string
        print('The stack is: {}'.format(sstr))

    def push(self, data):
        '''
        Function to insert an element at the beginning of the stack
        '''

        if self.head == None:
            self.head = Node(data)
            return

        itr = self.head

        while itr.nxt:
            itr = itr.nxt

        new_node = Node(data)
        itr.nxt = new_node

    def insert_vals(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        '''
        Function to get the length of the linked list
        '''

        itr = self.head
        len = 0

        while itr:
            len = len + 1
            itr = itr.nxt
        return len

    def pop(self):
        '''
        Function to pop an element from the stack
        '''
        # popping the last element

        if self.head == None:
            print('Cannot pop from empty stack')
            return
        itr = self.head

        count = 0

        while count < self.get_len() - 2:
            count = count + 1
            itr = itr.nxt

        removed = itr.nxt.data
        itr.nxt = None
        return removed

    def get_max(self):
        if self.get_len() <= 0:
            print('The stack is empty')
            return None
        else:
            max = -10000000
            itr = self.head
            for i in range(self.get_len()):
                if itr.data > max:
                    max = itr.data
                    itr = itr.nxt
            return max


if __name__ == '__main__':
    n = int(input('Enter n: '))
    stck = Stack()
    for i in range(n):
        query = list(map(int, input('Enter the query \n1. push - enter 1 <element to be pushed> e.g.: 1 23\n2. pop\n3. get max element\n4. quit \n').split()))
        if query[0] == 4:
            exit
        elif query[0] == 1:
            if len(query) != 2:
                print('The input format is wrong, please enter the input again.')
            else:
                stck.push(query[1])
        elif query[0] == 2:
            stck.pop()
        elif query[0] == 3:
            print('The maximum element in the stack is: {}'.format(stck.get_max()))
        else:
            print('Wrong input. Please try again.')
            exit
    
                
            
stck.print_stack()