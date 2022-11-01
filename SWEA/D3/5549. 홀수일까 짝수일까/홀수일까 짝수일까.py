T = int(input())

def sol():

    n = input()

    if int(n[-1]) % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
 
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')