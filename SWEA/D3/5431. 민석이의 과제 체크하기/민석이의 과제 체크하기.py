T = int(input())

def sol():
    n, k = map(int, input().split())
    completed = list(map(int, input().split()))
    inCompleted = [str(i) for i in range(1, n+1) if i not in completed]
    return ' '.join(inCompleted)
 
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')