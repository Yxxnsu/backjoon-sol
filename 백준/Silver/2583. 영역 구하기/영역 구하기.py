import sys
sys.setrecursionlimit(10**5)

N, M, K = map(int, input().split())

matrix = [[1] * M for _ in range(N)]
li = [list(map(int, input().split())) for _ in range(K)]

def paintMatrix():
    global matrix
    for v in li:
        x1,y1,x2,y2 = v
    
        o_x1 = N - y1 - 1
        o_y1 = x1
        o_x2 = N - y2
        o_y2 = x2
    
        for i in range(o_x2, o_x1+1):
            for j in range(o_y1, o_y2):
                if matrix[i][j] == 1:
                    matrix[i][j] = 0    
    return matrix

def dfs(x, y):
    global k
    if matrix[x][y] != 0:
        matrix[x][y] = 0
        k += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                dfs(nx, ny)
        return 1
    return 0


matrix = paintMatrix()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

k, area = 0, 0
extent = []
for i in range(N):
    for j in range(M):
        dfs(i, j)
        if k > 0:
            extent.append(k)
            area += 1
        k = 0
extent.sort()
print(area)
print(*extent, sep=' ')
