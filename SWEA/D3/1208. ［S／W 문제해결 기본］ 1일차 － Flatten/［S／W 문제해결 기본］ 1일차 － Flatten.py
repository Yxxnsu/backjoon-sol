T = 10

def sol():

    N = int(input())
    li = list(map(int, input().split()))
    li.sort()

    for _ in range(N):
        li[-1] -= 1
        li[0] += 1
        li.sort()
    
    return li[-1] - li[0]
    

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')