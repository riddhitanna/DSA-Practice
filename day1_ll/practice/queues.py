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


class Queue:

    '''
    Class to implement the functions of a linked list
    '''

    def __init__(self):

        # initialize head to none
        self.head = None

    def print_q(self):
        '''
        Function to print the elements of the linked list
        '''

        # check if linked list is empty
        if self.head == None:
            print("Linked List is empty.")
            return

        # iterate through linked list
        itr = self.head
        qstr = ''

        # append all elements to string
        while itr:
            # print(itr.data)
            qstr = qstr + str(itr.data) + '->'
            itr = itr.nxt

        # print the string
        print(qstr)

    def push(self, data):
        '''
        Function to insert an element at the end of the queue
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
        # popping the first element

        if self.head == None:
            print('Cannot pop from empty stack')
            return
        itr = self.head


        removed = itr.data
        self.head = itr.nxt
        return removed


if __name__ == '__main__':
    que = Queue()
    que.push(10)
    que.push(15)
    que.push(20)
    que.print_q()
    print('{} popped from queue'.format(que.pop()))
    que.print_q()
