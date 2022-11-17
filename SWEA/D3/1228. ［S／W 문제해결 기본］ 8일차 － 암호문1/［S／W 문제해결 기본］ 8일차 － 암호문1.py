from collections import deque

T = 10

def sol():

    N = int(input())
    li = list(input().split())
    K = int(input())
    command = list(input().split())

    for i, v in enumerate(command):
        if v == 'I':
            start = i + 3
            end = start + int(command[i+2])
            s = command[start:end]

            for k in s[::-1]:
                li.insert(int(command[i+1]), k)
    
    return ' '.join(li[:10])

ans = []
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')