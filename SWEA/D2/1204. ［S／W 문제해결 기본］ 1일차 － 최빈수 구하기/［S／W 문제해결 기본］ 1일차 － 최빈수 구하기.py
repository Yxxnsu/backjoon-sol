T = int(input())

for idx in range(1, T+1):
	t_case_num = int(input())	
	cnt_num_list = [0] * 101
	num_list = list(map(int, input().split()))

	for v in num_list:
		cnt_num_list[v] += 1

	i = 0
	max_value = max(cnt_num_list)
	for index,v in enumerate(cnt_num_list):
		if v == max_value:
			i = index
	print(f'#{t_case_num} {i}')