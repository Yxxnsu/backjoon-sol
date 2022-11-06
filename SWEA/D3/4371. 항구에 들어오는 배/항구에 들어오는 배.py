from collections import deque

T = int(input())

def sol():
    
    N = int(input())
    li = [int(input()) for _ in range(N)]
    
    q = deque([v-1 for v in li if v != 0])
    q.popleft()

    ans = 0
    while q:
        k = q.popleft()
        q = deque([v for v in q if v % k != 0])
        ans += 1
    return ans
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')