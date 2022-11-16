from collections import deque
import sys

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
tomato = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    global tomato

    while tomato:
        n, m = tomato.popleft()
        for i in range(4):
            nx = n + dx[i]
            ny = m + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                tomato.append([nx,ny])
                graph[nx][ny] = graph[n][m] + 1

BFS()

ans = 0
for v in graph:
    if 0 in v:
        print(-1)
        sys.exit(0)
    ans = max(ans,max(v))
print(ans-1)