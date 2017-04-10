def is_multiple(n, m):
    for i in range(1, n+1):
        if n == i * m:
            return True
    return False

if __name__ == '__main__':
    print(is_multiple(10,2))
    print(is_multiple(21, 4))
    