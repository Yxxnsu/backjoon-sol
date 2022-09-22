board = input()
mino = ['AAAA','BB']

def greedy(board):

	if "." in board:
		return "."
	
	l = len(board)
	
	a = l // 4
	b = l % 4 // 2
	l = l % 4 % 2

	if l != 0:
		return -1
	else:
		return mino[0] * a + mino[1] * b

if board.count(".") == 0:
	s = greedy(board)
	print(s)

else:
	s = ''
	i = 0
	start = end = 0
	while i < len(board):
		if i == len(board) - 1 and board[i] != ".":
			if greedy(board[start:]) != -1:
				s += greedy(board[start:])
			else:
				i = -1
			break
		
		elif board[i] == '.':

			# 문자열의 끝점 갱신, 카운트한 점의 개수 초기화
			disturb, end = 0, i

			# "." 이전의 문자 확인하기
			translate = greedy(board[start:end])

			# 확인해서 충족하면 변환한 문자열 저장
			if translate != -1:
				s += translate
			else:
				i = -1
				break
			
			# 점 건너뛰기
			while True:
				if i == len(board):
					break
				elif board[i] == '.':
					disturb += 1
					i += 1
				else:
					break

			# 시작점 갱신
			start = i
			s += "." * disturb
		else:
			i += 1
			
	print(s) if i != -1 else print(-1)		
			
		
			
				
				
		
		
	
			
		
			
			
			

		
	
		
		
