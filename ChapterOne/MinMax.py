'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise R-1.3
--------------
Write a short Python function, minmax(data), that takes a 
sequence of one or more numbers and returns the smallest
and largest numbers, in the form of a tuple of length two.
Do not use the built in min or max functions.
--------------
author Tatyana Royer
--------------
'''

def minmax(data):
    min = data[0]
    max = data[0]

    # find the min value in data
    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
    
    # find the max value in data
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    
    # returns the values as a tuple
    return (min, max)

if __name__ == '__main__':
    list = [4, 24, 5, 16, 1, 72, 45]

    result = minmax(list)

    # unpacks the tuple and assigns them to
    # minimum and maximum
    minimum = result[0]
    maximum = result[1]
    
    # prints the results
    print('Minimum is {0}'.format(minimum))
    print('Maximum is {0}'.format(maximum))
    
