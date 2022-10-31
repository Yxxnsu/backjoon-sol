T = int(input())

def isAscending(num):

    num_s = list(str(num))
    sort_num_s = sorted(num_s)

    return True if sort_num_s == num_s else False
        
def sol():
    n = int(input())
    num_list = list(map(int, input().split()))

    ans = -1
    for i in range(n):
        for j in range(i+1,n):
            product = num_list[i] * num_list[j]
            if product > ans:
                if isAscending(product):
                    ans = product if ans < product else ans
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')