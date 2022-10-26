T = int(input())
 
def sol():

    a, b = map(int, input().split())
    
    ans = 0
    for i in range(a, b+1):
        if int(i ** 0.5) ** 2 == i:
            sqrt = int(i ** 0.5)
            if str(sqrt) == str(sqrt)[::-1] and str(i) == str(i)[::-1]:
                ans += 1
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')