from collections import deque

s = input()
ucpc = deque(['U','C','P','C'])

for i in range(len(s)):
	if not ucpc:
		break
	if s[i] == ucpc[0]:
		ucpc.popleft()
	else:
		continue

if len(ucpc) == 0:
	print('I love UCPC')
else:
	print('I hate UCPC')
		
	
	
	
		