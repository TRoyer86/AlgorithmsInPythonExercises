'''
Data Structures and Algorithms in Python by Goodrich
--------------
Exercise C-1.13
--------------
Create a function that reverses a list of elements.
--------------
author Tatyana Royer
--------------
'''

def reverse_seq(A):
    lindex = 0
    rindex = len(A) - 1
    temp = 0

    # if there are an even number of elements in A
    if (len(A) % 2 == 0):
        while lindex < rindex:
            # swap
            temp = A[lindex] # store data from A[lindex] in temp
            A[lindex] = A[rindex] # data from A[rindex] goes to A[lindex]
            A[rindex] = temp # stored data in temp goes to A[rindex]
            lindex += 1 # move lindex up one
            rindex -= 1 # move rindex down one
    else:
        mid = (lindex + rindex) / 2
        while lindex != mid:
            # swap
            temp = A[lindex] # store data from A[lindex] in temp
            A[lindex] = A[rindex] # data from A[rindex] goes to A[lindex]
            A[rindex] = temp # stored data in temp goes to A[rindex]
            lindex += 1 # move lindex up one
            rindex -= 1 # move rindex down one
    return A

if __name__ == '__main__':

    dataeven = [5, 12, 25, 16, 1, 11]
    print('Reversing a sequence with an even number of elements:')
    print(reverse_seq(dataeven))

    dataodd = [5, 12, 25, 16, 1]
    print('Reversing a sequence with an odd number of elements:')
    print(reverse_seq(dataodd))

    datastring = ['A', 'X', 'C', 'Q', 'hello', 'wuzzup']
    print('Reversing a sequence with strings for elements:')
    print(reverse_seq(datastring))

            

    