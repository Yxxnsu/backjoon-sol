T = int(input())

def sol():
    li = list(map(int, input().split()))

    a = li[0] / li[1] * 100
    b = li[2] / li[3] * 100

    if a > b: return 'ALICE'
    elif a < b: return 'BOB'
    return 'DRAW'

ans = []
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')