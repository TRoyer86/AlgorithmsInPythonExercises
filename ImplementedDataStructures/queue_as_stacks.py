from stackclass import Stack

class QueueStacks:

    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()
    
    def enqueue(self, element):
        self.instack.elements.append(element)
    
    def dequeue(self):
        # this iterates through the input stack and transfers
        # the values into the output stack
        for i in range(len(self.instack.elements)):
            temp = self.instack.elements.pop()
            self.outstack.elements.append(temp)
        # when the output stack is popped, it stores the
        # correct value in a variable called popped
        popped = self.outstack.elements.pop()
        # this puts the elements in the output stack back into
        # the input stack
        for i in range(len(self.outstack.elements)):
            temp = self.outstack.elements.pop()
            self.instack.elements.append(temp)
        # this returns the element to be dequeued
        return popped

    def isEmpty(self):
        return self.instack.elements == []
    
    def size(self):
        return len(self.instack.elements)