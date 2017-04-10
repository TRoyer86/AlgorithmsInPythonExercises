'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise R-1.6
--------------
Write a short Python function, sum_of_squares(n), that
takes a positive integer, n, and returns the sum of
the squares of all the odd positive integers smaller than n.
--------------
author Tatyana Royer
--------------
'''

def sum_of_odd_squares(n):
    sum = 0
    for i in range(0,n):
        # if i is odd
        if (i % 2) != 0:
            # sum is sum + i^2
            sum += (i**2)
    return sum

if __name__ == '__main__':    

    num = int(input('Enter a positive integer: '))
    print(sum_of_odd_squares(num))

