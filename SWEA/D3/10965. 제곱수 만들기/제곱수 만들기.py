T = int(input())    

def sol():
    n = int(input())
    ans = 1

    if p_list[0][n]:
        return n
    
    i, cnt = 0, 0
    while n > 1:
        if n % p_list[1][i] == 0:
            cnt += 1
            if n // p_list[1][i] == 1 and cnt % 2 != 0:
                ans *= n
                break
            n //= p_list[1][i]
        else:
            if cnt % 2 != 0:
                ans *= p_list[1][i]            
            if p_list[0][n]:
                ans *= n
                break
            i += 1
            # if i == len(p_list[1]):
            #     ans *= n
            #     break
            cnt = 0
    return ans 

def prime_list(n):
    seive = [True] * n
    m = int(n ** 0.5) + 1

    for i in range(2, m):
        if seive[i] == True:
            for j in range(i+i, n, i):
                seive[j] = False
    return [seive,[i for i in range(2, n) if seive[i] == True]]

p_list = prime_list(10000001)
result = []
for tc in range(1, T+1):
    result.append(f'#{tc} {sol()}')
for v in result:
    print(v)