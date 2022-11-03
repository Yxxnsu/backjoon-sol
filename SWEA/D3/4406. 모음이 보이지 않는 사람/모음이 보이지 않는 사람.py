T = int(input())

def sol():

    s = input()

    ans = ''
    for v in s:
        if v in ('a','e','i','o','u'):
            continue
        else:
            ans += v
    return ans
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')