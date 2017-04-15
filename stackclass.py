#!/usr/bin/env python

'''
Implementation of a Stack using lists
'''

class Stack:

    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) <= 0:
            return None
        return self.elements.pop()
    
    def peek(self):
        return self.elements[len(self.elements)-1]

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)
    
