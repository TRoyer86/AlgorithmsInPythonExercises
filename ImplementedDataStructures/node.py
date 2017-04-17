class Node:

    # Each Node contains data and a next value that
    # points to another Node
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev






