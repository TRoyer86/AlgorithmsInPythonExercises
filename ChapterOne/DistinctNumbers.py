'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise C-1.15
--------------
Write a function that takes a sequence of integer values
and determines if each element is distinct.
--------------
author Tatyana Royer
--------------
'''

def distinct(A):
    count = 0
    for first in range(len(A)):
        for second in range(first + 1, len(A)):
            if A[first] == A[second]:
                return False
    return True

if __name__ == '__main__':

    # test data
    list1 = [1,2,3,4,5,6,7,8]
    list2 = [1,2,3,4,3,5,7,9]

    print(distinct(list1))
    print(distinct(list2))

    