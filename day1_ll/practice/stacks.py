'''
Contains practice implementation of stacks in Python.

Date: 24-Jan-2022
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
    Class to implement the functions of a linked list
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
            print("Linked List is empty.")
            return

        # iterate through linked list
        itr = self.head
        llstr = ''

        # append all elements to string
        while itr:
            # print(itr.data)
            llstr = llstr + str(itr.data) + '->'
            itr = itr.nxt

        # print the string
        print(llstr)

    def push(self, data):
        '''
        Function to insert an element at the end of the linked list
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
        Function to remove an element at the given index from linked list
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


if __name__ == '__main__':
    stck = Stack()
    stck.push(10)
    stck.push(15)
    stck.push(20)
    stck.print_stack()
    print('{} popped from stack'.format(stck.pop()))
    stck.print_stack()
