#!/usr/bin/env python

'''
Implementation of a Queue using lists
'''

class Queue:

    def __init__(self):
        self.elements = []
    
    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if len(self.elements) > 0:
            element = self.elements[0]
            self.elements = self.elements[1:len(self.elements)]
            return element
        else:
            return None
    
    def isEmpty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

