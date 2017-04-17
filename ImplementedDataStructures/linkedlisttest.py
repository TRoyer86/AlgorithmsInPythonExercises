'''
Tests the implementation of the linked list and node classes
'''

from linkedlist import LinkedList

mylist = LinkedList()

print(mylist.isEmpty())
print(mylist.size())

mylist.insert('W')
mylist.insert('E')
mylist.insert('S')
mylist.insert('L')
mylist.insert('E')
mylist.insert('Y')

print(mylist.size())

print(mylist.search('S'))

mylist.delete('S')

print(mylist.size())


