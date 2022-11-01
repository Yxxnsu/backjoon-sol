import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def make_graph():

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def dfs(i):
    visited[i] = 1
    for k in graph[i]:
        if visited[k] == 0:
            dfs(k)
    return False

graph = make_graph()

ans = 0
for i in range(1, n+1): 
    if visited[i] == 0:
        ans += 1
        dfs(i)

print(ans)