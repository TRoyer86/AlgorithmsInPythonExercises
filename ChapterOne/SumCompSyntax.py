'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise R-1.5
--------------
Give a single command that computes the sum from 
Exercise R-1.4, relying on Python's comprehension syntax and
the built-in sum function.
--------------
author Tatyana Royer
--------------
'''

def sum_of_squares(n):
    return sum(i**2 for i in range(0,n))

if __name__ == '__main__':
    print(sum_of_squares(int(input('Enter a positive integer: '))))

    
    