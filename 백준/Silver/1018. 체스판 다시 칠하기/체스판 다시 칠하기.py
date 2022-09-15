def num_have_to_colored(l):
	white = [
		"WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW",
		"WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW",	
	]
	black = [
		"BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB",
		"BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB",	
	]

	c_black, c_white = 0, 0
	
	for i in range(8):
		for j in range(8):
			if l[i][j] != white[i][j]:
				c_white += 1
			if l[i][j] != black[i][j]:
				c_black += 1

	return c_black if c_white > c_black else c_white

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
diff_w, diff_h = m - 8, n - 8
min = 65

for i in range(diff_w + 1):
	for j in range(diff_h + 1):
		l = []
		for k in range(8):
			l.append(matrix[j+k][i:i+8])
		if min > num_have_to_colored(l):
			min = num_have_to_colored(l)
print(min)		

