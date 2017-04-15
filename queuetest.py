#!/usr/bin/env python

from queueclass import Queue

if __name__ == '__main__':

    myqueue = Queue()

    print(myqueue.size())

    print(myqueue.isEmpty())

    # Add each letter in the name of the cutest soon to be 2 year old
    myqueue.enqueue('J')
    myqueue.enqueue('O')
    myqueue.enqueue('S')
    myqueue.enqueue('H')

    print(myqueue.size())

    # And it returns his name in order
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())

    print(myqueue.size())

    print(myqueue.isEmpty())

    # Add each letter in the name of the best big brother in the world
    myqueue.enqueue('W')
    myqueue.enqueue('E')
    myqueue.enqueue('S')

    print(myqueue.size())

    # And again, it dequeues in order
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())

    print(myqueue.size())

    print(myqueue.isEmpty())
