T = int(input())

for idx in range(1, T+1):
	num_list = list(map(int, input().split()))
	min_value = min(num_list)
	max_value = max(num_list)
	sum = 0
	for v in num_list:
		if v == min_value or v == max_value:
			continue
		else:
			sum += v

	print(f'#{idx} {round(sum / (len(num_list)-2))}')
			