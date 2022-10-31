T = int(input())

def sol():
    
    n, m = map(int, input().split())
    li = [list(map(int,input().split())) for _ in range(m)]
    
    graph = [[] for _ in range(n+1)]
    for a, b in li:
        graph[a].append(b)
        graph[b].append(a)
    
    ans = 0
    for i in range(1, n+1):
        for j in graph[i]:
            for k in graph[j]:
                if k in graph[i]:
                    ans += 1
    return ans // 6
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')