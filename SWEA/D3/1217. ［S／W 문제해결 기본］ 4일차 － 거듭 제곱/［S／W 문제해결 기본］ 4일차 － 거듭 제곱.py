T = 10

def sol():

    tc = int(input())
    a, b = map(int, input().split())
    
    def recursion(n, m):
        if m == b:
            return 1
        return recursion(n, m+1) * n;
    
    ans = recursion(a, 0)
    return ans
    

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')