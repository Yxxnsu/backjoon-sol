T = int(input())

def LCS(x, y):
    x, y = ' ' + x, ' ' + y
    m, n = len(x), len(y)

    dp = [[0] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

for tc in range(1, T+1):
    a, b = input().split()

    ans = LCS(a, b)
    
    print(f'#{tc} {ans[-1][-1]}')