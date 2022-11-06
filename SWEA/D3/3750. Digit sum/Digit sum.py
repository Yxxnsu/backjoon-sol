T = int(input())

def sol():
    
    n = input()

    while len(n) != 1:
        sum = 0
        for v in n:
            sum += int(v)
        n = str(sum)
    
    return n
ans = []
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')