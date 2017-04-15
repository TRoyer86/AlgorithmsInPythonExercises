#!/usr/bin/env python

from stackclass import Stack

if __name__ == '__main__':

    test_stack = Stack()

    # This should be true
    print(test_stack.isEmpty())

    test_stack.push('W')
    test_stack.push('E')
    test_stack.push('S')

    print(test_stack.size())

    print(test_stack.peek())

    popped = test_stack.pop()
    print(popped)

    popped = test_stack.pop()
    print(popped)

    popped = test_stack.pop()
    print(popped)

    print(test_stack.isEmpty())

    print(test_stack.size())

    # This tests the empty stack condition
    popped = test_stack.pop()
    print(popped)

    print(test_stack.isEmpty())
