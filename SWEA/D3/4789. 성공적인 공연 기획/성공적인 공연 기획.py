T = int(input())

def sol():

    li = input()

    ans, clap = 0, 0
    for i in range(len(li)):
        if int(li[i]) > 0:
            if i == 0:
                clap += int(li[i])
            else:
                if clap < i:
                    addt = i - clap
                    ans += addt
                    clap += addt + int(li[i])
                else:
                    clap += int(li[i])
    return ans
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')