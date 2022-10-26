for num in range(int(input())):
    n = int(input())-1
 
    while True:
        if n % 2 == 1:
            n = n//2
 
        if n % 4 == 0:
            ans = 0
            break
        elif n % 2 == 0:
            ans = 1
            break
    print(f'#{num+1}',ans)