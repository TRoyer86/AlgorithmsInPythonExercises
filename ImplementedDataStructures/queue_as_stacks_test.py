from queue_as_stacks import QueueStacks

if __name__ == '__main__':

    test = QueueStacks()

    print(test.isEmpty())

    test.enqueue('W')
    test.enqueue('E')
    test.enqueue('S')

    print(test.size())

    print(test.dequeue())

    print(test.size())
    print(test.isEmpty())

    print(test.dequeue())
    print(test.dequeue())

    print(test.size())
    print(test.isEmpty())
