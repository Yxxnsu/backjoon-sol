s = input()
t = input()

while s != t:
	len_t = len(t)
	
	if (len_t == len(s) and s != t):
		break
		
	if t[-1] == 'A':
		t = t[:len_t-1]
	else:
		t = t[:len_t-1]
		t = t[::-1]

if s == t:
	print(1)
else:
	print(0)
	
		