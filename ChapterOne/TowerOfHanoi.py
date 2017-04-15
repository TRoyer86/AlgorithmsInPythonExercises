def hanoi(n, beg, aux, end):
    if n == 1:
        print('{0} --> {1}'.format(beg, end))
    else:
        hanoi(n-1, beg, end, aux)
        hanoi(1, beg, aux, end)
        hanoi(n-1, aux, beg, end)

if __name__ == '__main__':
    n = int(input('How many disks are used?'))
    beg = 'A'
    aux = 'B'
    end = 'C'

    hanoi(n, beg, aux, end)
