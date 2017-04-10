'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise R-1.4
--------------
Write a short Python function, sum_of_squares(n), that
takes a positive integer, n, and returns the sum of
the squares of all the positive integers smaller than n.
--------------
author Tatyana Royer
--------------
'''

def sum_of_squares(n):
    sum = 0
    for i in range(0, n):
        sum += (i**2)
    return sum

if __name__ == '__main__':
    sumofsquares = sum_of_squares(int(input('Enter a positive integer: ')))

    print(sumofsquares)
    