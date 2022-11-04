from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0] * (N + 1)
visited = [False] * (N + 1)

def bfs():
    
    global visited, ans
    
    q = deque()    
    q.append(1)
    visited[1] = True

    while q:
        parent = q.popleft()        
        for v in graph[parent]:
            if not visited[v]:
                visited[v] = True
                ans[v] = parent
                q.append(v)                
bfs()
print(*ans[2:], sep='\n')