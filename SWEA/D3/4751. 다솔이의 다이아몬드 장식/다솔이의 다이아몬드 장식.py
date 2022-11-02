T = int(input())

def sol():

    s = input()

    matrix = [[''] * (5 * len(s) - (len(s) - 1)) for i in range(5)]

    j = 0
    for i in range(2, len(matrix[0]), 4):
        matrix[2][i] = s[j]

        matrix[2][i-2] = '#'
        matrix[2][i+2] = '#'
        matrix[2][i-1] = '.'
        matrix[2][i+1] = '.'
        matrix[1][i] = '.'
        matrix[3][i] = '.'
        matrix[1][i-1] = '#'
        matrix[1][i+1] = '#'
        matrix[3][i-1] = '#'
        matrix[3][i+1] = '#'
        matrix[0][i] = '#'
        matrix[4][i] = '#'
        j += 1

    for i in range(5):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '':
                matrix[i][j] = '.'
    
    for v in matrix:
        print(*v, sep="")
    
for tc in range(1, T+1):
    sol()