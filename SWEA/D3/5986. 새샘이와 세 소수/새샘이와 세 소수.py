T = int(input())

def prime_list(n):
    
    seive = [True] * n
    m = int(n ** 0.5) + 1
    
    for i in range(2, m):
        if seive[i] == True:
            for j in range(i+i, n, i):
                seive[j] = False
    return [i for i in range(2, n) if seive[i] == True]

def sol():

    n = int(input())
    l_prime = prime_list(n)

    ans = 0
    for i in range(len(l_prime)):
        for j in range(i, len(l_prime)):
            for k in range(j, len(l_prime)):
                if l_prime[i] + l_prime[j] + l_prime[k] == n:
                    ans += 1
                    break
                if l_prime[i] + l_prime[j] + l_prime[k] > n:
                    break
                if l_prime[k] > n:
                    break
            if l_prime[j] > n:
                break
        if l_prime[i] > n:
            break
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')