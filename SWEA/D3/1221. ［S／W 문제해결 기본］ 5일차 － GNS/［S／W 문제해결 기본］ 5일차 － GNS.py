T = int(input())

def sol(tc):

    num_list = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    length = input(f'#{tc} ')
    s = input().split()

    ans = ''
    for num in num_list:
        ans += f'{num} ' * s.count(num)
    ans.rstrip(' ')
    return ans

for tc in range(1, T+1):
    print(f'#{tc}\n{sol(tc)}')