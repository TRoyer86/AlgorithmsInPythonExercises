from node import Node

class LinkedList:

    # the list has a head initialized to None
    def __init__(self, head=None):
        self.head = head

    def isEmpty(self):
        return self.head == None

    def search(self, key):
        # x initially refers to the head of the list
        x = self.head
        # while x is not None and the key does not match
        # the data in x, go to the next node and try
        while x != None and x.data != key:
            x = x.next
        return x

    def size(self):
        # x is initially the head of the list
        x = self.head
        count = 0
        # while x is a node in the list
        while x != None:
            count = count + 1
            x = x.next
        return count

    def insert(self, key):
        # x is a new node with key passed into the data field
        # and it points to the head node in its next field
        x = Node(key, self.head)
        # if there is already a head node, set that head node's
        # prev field to point to node x
        if self.head != None:
            self.head.prev = x
        # node x is now the new head node
        self.head = x


    def delete(self, key):
        # x is the resulting node of calling the search function
        # with value key
        x = self.search(key)
        # update pointers
        # if x is not the head of the list, make the previous
        # node point to the node that follows x
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        # if x points to another node, that node's prev field
        # now points to the node before x
        if x.next != None:
            x.next.prev = x.prev





