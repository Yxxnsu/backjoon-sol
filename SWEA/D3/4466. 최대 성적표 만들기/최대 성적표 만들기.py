T = int(input())

def sol():
    
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort(reverse=True)

    ans = 0
    for i in range(K):
        ans += li[i]
    return ans
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')