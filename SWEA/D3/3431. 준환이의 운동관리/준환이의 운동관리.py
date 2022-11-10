T = int(input())

def sol():
    
    L, U, X = map(int, input().split())

    if X > U:
        return -1
    elif L <= X <= U:
        return 0
    else:
        return L - X

ans = []
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')