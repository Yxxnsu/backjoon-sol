from collections import deque

N = int(input())
a, b = map(int, input().split())
M = int(input())
li = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for x, y in li:
    graph[x].append(y)
    graph[y].append(x)

def BFS(a):
    global ans, visited
    q = deque()
    q.append([a,0])
    while q:
        k, floor = q.popleft()
        ans = floor + 1
        for v in graph[k]:
            if not visited[v]:
                visited[v] = True
                if v == max_v:
                    return 1
                q.append([v,ans])
    return 0
ans = 0
min_v = min(a,b)
max_v = max(a,b)
find = BFS(min_v)

print(-1 if not find else ans)
