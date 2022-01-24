'''
Contains practice implementation of Linked Lists in Python. 

Date: 24-Jan-2022
'''


class Node:

    '''
    Individual node of a linked list
    '''

    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:

    '''
    Class to implement the functions of a linked list
    '''

    def __init__(self):

        # initialize head to none
        self.head = None

    def insert_at_beg(self, data):
        '''
        Function to insert element at the beginning of the linked list
        '''

        # create a new node and link it to the head
        node = Node(data, self.head)
        # change the head of the list to the new node
        self.head = node

    def print_ll(self):
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
        print('The linked list is: {}'.format(llstr))

    def insert_at_end(self, data):
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

    def remove_at(self, index):
        '''
        Function to remove an element at the given index from linked list
        '''

        # check if index is valid
        if index < 0 or index > self.get_len():
            raise Exception('Index  does not exist')

        # removing element at the head
        if index == 0:
            self.head = self.head.nxt
            return

        # iterating to find the index
        count = 0
        itr = self.head
        while itr:
            if count+1 == index:
                itr.nxt = itr.nxt.nxt
                break
            itr = itr.nxt
            count = count + 1

    def insert_at(self, index, data):
        '''
        Function to insert an element at index
        '''

        # check if index is valid
        if index < 0 or index > self.get_len():
            raise Exception('Index  does not exist')

        if index == 0:
            self.insert_at_beg(data)
            return

        count = 0
        itr = self.head

        while itr.nxt:
            if count + 1 == index:
                new_node = Node(data)
                new_node.nxt = itr.nxt
                itr.nxt = new_node
            count = count + 1
            itr = itr.nxt


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beg(10)
    # ll.insert_at_beg(11)
    ll.insert_at_end(14)
    ll.insert_vals([14, 21, 34])
    ll.insert_at(2, 23)
    ll.print_ll()
