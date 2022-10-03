N = int(input())
dice = list(map(int,input().split()))

min1 = min(dice[0],dice[5])
min2 = min(dice[1],dice[4])
min3 = min(dice[2],dice[3])

min_list = [min1,min2,min3]
min_list.sort()

min1 = min_list[0]
min2 = min1 + min_list[1]
min3 = min2 + min_list[2]

if N == 1:
	print(sum(dice)-max(dice))
else:
	print(4 * min3 + (8 * N - 12) * min2 + (5 * N**2 - 16 * N + 12) * min1)
	