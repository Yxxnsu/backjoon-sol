import sys
sys.setrecursionlimit(10**5)

N = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

matrix = [list(input()) for _ in range(N)]
matrix1 = []
for v in matrix:
    k = v.copy()
    matrix1.append(k)
    
def dfs(x, y, option, element):

    if option == 1:
        if matrix[x][y] != 'x':
            if matrix[x][y] == element:
                matrix[x][y] = 'x'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        dfs(nx, ny, 1, element)
                return True        
            return False
        else:
            return False

    else:
        if matrix1[x][y] != 'x':
            if element in ('R','G'):
                if matrix1[x][y] == 'R' or matrix1[x][y] == 'G':
                    matrix1[x][y] = 'x'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            dfs(nx, ny, 2, element)
                    return True
            else:
                if matrix1[x][y] == element:
                    matrix1[x][y] = 'x'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            dfs(nx, ny, 2, element)
                    return True
            return False
        else:
            return False

a, b = 0, 0
for i in range(N):
    for j in range(N):
        if dfs(i, j, 1, matrix[i][j]) == True:
            a += 1
        if dfs(i, j, 2, matrix1[i][j]) == True:
            b += 1
print(a, b) 
