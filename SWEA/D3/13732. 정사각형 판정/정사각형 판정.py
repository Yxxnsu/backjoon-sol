def is_square_number(N):
	return int(N ** 0.5) ** 2 == N

def find_square(matrix, N):
	global side
	for i in range(N):
		for j in range(N):
			if matrix[i][j] == '#':
				for h in range(side):
					for w in range(side):
						if matrix[i+h][j+w] != '#':
							return False
						else:
							matrix[i+h][j+w] = '.'
	return True	

T = int(input())

for idx in range(1, T+1):

	N = int(input())
	matrix = [list(input()) for _ in range(N)]
	sum_of_square = sum([x.count('#') for x in matrix])

	# if sum_of_square == 1:
		# print(f'#{idx} no')		
	if not is_square_number(sum_of_square):
		print(f'#{idx} no')
	else:
		side = int(sum_of_square ** 0.5)
		print(f'#{idx} {"yes" if find_square(matrix, N) else "no"}')