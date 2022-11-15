T = 10

def sol():

    tc = int(input())

    finding = input()
    s = input()

    return s.count(finding)

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')