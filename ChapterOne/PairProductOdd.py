'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise C-1.14
--------------
Write a function that takes a sequence of integer values
and determines if there is a distinct pair of numbers in 
the sequence whose product is odd.
--------------
author Tatyana Royer
--------------
'''

def pair_prod_odd(A):
    count = 0
    for first in range(len(A)):
        for second in range(first + 1, len(A)):
            product = A[first] * A[second]
            if (product % 2) != 0:
                count += 1
            if count > 1:
                # if there is more than one odd product
                return False
    # if there is only one odd product return True
    if count == 1:
        return True
    # if all products are even return False
    else:
        return False

if __name__ == '__main__':
    # test data 
    list1 = [2, 3, 1, 4]
    list2 = [2, 4, 6, 8]
    list3 = [1, 3, 5, 2]

    print('One distinct odd product')
    print(pair_prod_odd(list1))
    print('All products are even')
    print(pair_prod_odd(list2))
    print('More than one odd product')
    print(pair_prod_odd(list3))