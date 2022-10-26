T = int(input())
 
def sol():

    n, a, b = map(int, input().split())

    max_value = min(a, b)
    min_value = a + b - n if a + b > n else 0

    return f'{max_value} {min_value}'

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')