from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
l = [int(input()) for _ in range(N)]

stack = []
series = []
oper = []

tmp = sorted(l)

index = 0

for i in range(N):

	if tmp[i] == l[index]:
		stack.append(tmp[i])
		oper.append('+')
		series.append(stack.pop())
		oper.append('-')		
		index += 1

		if index == (N-1):
			while stack:
				series.append(stack.pop())
				oper.append('-')
		else:
			try:
				while (stack[-1] == l[index]) and stack:
					series.append(stack.pop())
					oper.append('-')
					index += 1
			except IndexError:
				pass			
	else:
		stack.append(tmp[i])
		oper.append('+')

if series == l:
	for i in range(len(oper)):
		print(oper[i])
else:
	print('NO')