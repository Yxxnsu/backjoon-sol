T = int(input())

def sol():

    a, b, c = map(int, input().split())

    ans1 = c // a
    ans2 = c // b

    r1 = ans1 + ((c % a) // b) if c % a >= b else ans1
    r2 = ans2 + ((c % b) // a) if c % b >= a else ans2

    return max(r1,r2)

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')