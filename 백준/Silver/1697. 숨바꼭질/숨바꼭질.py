from collections import deque

N, K = map(int, input().split())

M = 10 ** 5
dist = [0] * (M+1)

def BFS():
    q = deque()
    q.append(N)
    
    while q:
        v = q.popleft()
        if v == K:
            print(dist[v])
            break
        for next in (v-1, v+1, v*2):
            if 0 <= next <= M and not dist[next]:
                q.append(next)
                dist[next] = dist[v] + 1
BFS()