T = int(input())

def sol():

    N = int(input())
    li = ''

    while len(li) != N:
        l = list(input().split())
        li += ''.join(l)
    
    ans = 0
    while True:
        if li.find(str(ans)) == -1:
            return ans
        ans += 1
        
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')