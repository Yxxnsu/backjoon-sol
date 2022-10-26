T = int(input())
 
def sol():

    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
       for j in range(i+1, n):
            ia, ib = li[i]
            ja, jb = li[j]
            if (ia > ja and ib < jb) or (ja > ia and jb < ib):
                ans += 1
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')