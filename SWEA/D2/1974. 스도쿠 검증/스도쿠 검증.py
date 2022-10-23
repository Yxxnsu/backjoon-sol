T = int(input())

for idx in range(1, T+1):

	sudoku = [list(map(int,input().split())) for _ in range(9)]
	isSudoku_w = isSudoku_h = isSudoku_matrix = True
	
	for i in range(9):
		if len(set(sudoku[i])) != 9:
			isSudoku_w = False
			break
	
	for i in range(9):
		tmp = []
		for j in range(9):
			tmp.append(sudoku[j][i])
		if len(set(tmp)) != 9:
			isSudoku_h = False
			break
		tmp.clear()

	for i in range(0,9,3):
		for j in range(0,9,3):
			tmp = []
			for k in range(3):
				tmp += sudoku[i+k][j:j+3]
			if len(set(tmp)) != 9:
				isSudoku_matrix = False
				break
			tmp.clear()
		if isSudoku_matrix == False:
			break
	
	print(f'#{idx} {1 if isSudoku_w and isSudoku_h and isSudoku_matrix else 0}')
				
				
				
	