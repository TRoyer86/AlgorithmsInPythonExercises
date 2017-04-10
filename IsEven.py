'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise R-1.2
--------------
Write a short Python function, is_even(k), that takes
an integer value and returns True if k is even and False
if otherwise. However, your function cannot use the
multiplication, modulo, or division operators.
--------------
author Tatyana Royer
--------------
'''



def is_even(k):
    i = k
    
    # if k is 0
    if i == 0:
        return True;
    
    # if k is a positive integer
    if i >= 0:
        while i > 0:
            i = i - 2
            if i == 0:
                return True
        return False
    
    # if k is a negative integer
    if i < 0:
        while i < 0:
            i = i + 2
            if i == 0:
                return True
        return False

if __name__ == '__main__':
    
    '''
    print(is_even(20))
    print(is_even(15))
    print(is_even(50))
    print(is_even(101))
    '''
    
    num = int(input('Enter an integer.'))
    print('Is it even?')
    print(is_even(num))
    