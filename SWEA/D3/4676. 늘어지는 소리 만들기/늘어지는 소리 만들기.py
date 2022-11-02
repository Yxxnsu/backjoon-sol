T = int(input())

def sol():

    s = list(input())
    h = int(input())
    pos = list(map(int, input().split()))

    ans = ''
    for i in range(len(s)+1):
        if i == len(s):
            ans += '-' * (pos.count(i))
        else:
            ans += '-' * (pos.count(i))
            ans += s[i]
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')