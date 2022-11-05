import sys
sys.setrecursionlimit(10**5)

R, C = map(int, input().split())

matrix = [list(input()) for _ in range(R)]
visited = [0] * 26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 1

def dfs(x,y,k):    

    global visited, ans
    
    idx = ord(matrix[x][y]) - 65

    if visited[idx]: 
        return

    visited[idx] = 1
    ans = max(k, ans)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            dfs(nx, ny, k+1) 
    visited[idx] = 0

dfs(0, 0, ans)
print(ans)