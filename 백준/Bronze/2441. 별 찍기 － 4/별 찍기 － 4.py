N = int(input())

for i in range(N,-1,-1):
    print(' ' * (N-i), end = '')
    print('*' * i)