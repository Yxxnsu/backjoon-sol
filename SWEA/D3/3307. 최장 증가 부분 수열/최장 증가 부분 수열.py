T = int(input())

def sol():

    N = int(input())
    li = list(map(int, input().split()))
    
    dp = [0] * N
    dp[0] = 1

    for i in range(1, N):
        for j in range(i-1,-1,-1):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += 1

    return max(dp)

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')