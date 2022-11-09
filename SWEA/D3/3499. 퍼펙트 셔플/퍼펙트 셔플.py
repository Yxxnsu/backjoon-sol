T = int(input())

def sol():
    N = int(input())
    li = list(input().split())
    center = N // 2

    ans, front, back = [], [], []

    if N % 2 == 0:
        front = li[:center]
        back = li[center:]
    else:
        front = li[:center+1]
        back = li[center+1:]

    for i in range(center):
        ans.append(front[i])
        ans.append(back[i])
    
    if N % 2 == 1:
        ans.append(front[-1])

    return ' '.join(ans)


for tc in range(1, T+1):
    print(f'#{tc} {sol()}')