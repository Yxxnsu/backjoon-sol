T = int(input())
 
def sol():

    n = int(input())
    li = list(map(int, input().split()))
    avg = sum(li) / n
    ans = [v for v in li if avg >= v]
    return len(ans)

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')