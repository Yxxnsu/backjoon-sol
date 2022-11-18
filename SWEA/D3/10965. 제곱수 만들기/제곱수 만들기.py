T = int(input())

def sol():

    N = int(input())

    if prime_list[0][N]:
        return N

    ans, cnt, i = 1, 0, 0
    while N > 1:

        if N % prime_list[1][i] != 0:

            if cnt % 2 != 0:
                ans *= prime_list[1][i]
            
            if prime_list[0][N]:
                return ans * N
            
            i += 1
            cnt = 0

        else:
            N //= prime_list[1][i]
            cnt += 1

            if N == 1 and cnt % 2 != 0:
                return ans * prime_list[1][i]
            
    return ans

def prime_number(n):
    seive = [True] * n
    m = int(n ** 0.5) + 1

    for i in range(2, m):
        if seive[i]:
            for j in range(i+i, n, i):
                if seive[j]: seive[j] = False
    
    return [seive, [i for i in range(2, n) if seive[i] == True]]

prime_list = prime_number((10 ** 7) + 1)
ans = []
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')