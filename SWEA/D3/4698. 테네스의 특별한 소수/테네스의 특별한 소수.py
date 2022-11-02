T = int(input())

def prime_list(n):
    
    seive = [True] * n
    m = int(n ** 0.5) + 1

    for i in range(2, m):
        if seive[i] == True:
            for j in range(i+i, n, i):
                seive[j] = False
    return [i for i in range(2,n) if seive[i] == True]

def sol():

    d, a, b = input().split()
    p_list = prime_list(int(b)+1)

    ans = 0
    for i in range(len(p_list)):
        if int(a) <= p_list[i] <= int(b):
            s = str(p_list[i])
            if d in s:
                ans += 1
    return ans 

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')