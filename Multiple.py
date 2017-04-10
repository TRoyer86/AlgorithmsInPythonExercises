'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise R-1.1
--------------
Write a short Python function, is_multiple(n, m) 
that takes two integer values and returns True 
if n is a multiple of m.
'''

def is_multiple(n, m):
    for i in range(1, n+1):
        if n == i * m:
            return True
    return False

if __name__ == '__main__':
    print(is_multiple(10,2))
    print(is_multiple(21, 4))
