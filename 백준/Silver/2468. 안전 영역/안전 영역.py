import sys
sys.setrecursionlimit(10**5)

N = int(input())

height = []
matrix = [list(map(int, input().split())) for _ in range(N)]

max_h = 0

for v in matrix:
    if max_h < max(v):
        max_h = max(v)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h):
    if matrix[x][y] != 0:
        if matrix[x][y] <= h:
            matrix[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    dfs(nx, ny, h) 
            return True       
    return False

def dfsCheckArea(x,y,h):
    if n_matrix[x][y] != 0:
        if n_matrix[x][y] <= h:
            n_matrix[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    dfsCheckArea(nx,ny,h)
            return True
    return False

ans = []
for h in range(0,max_h+1):
    area = 0
    for i in range(N):
        for j in range(N):
            dfs(i,j,h)
    n_matrix = []
    for v in matrix:
        k = v.copy()
        n_matrix.append(k)
    for i in range(N):
        for j in range(N):
            if dfsCheckArea(i,j,100) == True:
                area += 1
    ans.append(area)
print(max(ans))

  # print(f'h is {h}')
    # for v in matrix:
    #     print(v)
    # print(f'area is {area}')