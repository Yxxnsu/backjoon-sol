T = 10

def sol():

    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    ans = 0
    for i in range(100):
        w, h = 0, 0
        for j in range(100):
            w += matrix[i][j]
            h += matrix[j][i]
        ans = max(ans, w, h) 

    c, r_c = 0, 0
    for j in range(100):
        c += matrix[j][j]
        r_c += matrix[j][99-j]
    
    ans = max(c, r_c, ans)

    return ans
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')