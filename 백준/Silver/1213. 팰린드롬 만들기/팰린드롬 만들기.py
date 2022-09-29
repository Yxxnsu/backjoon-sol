from itertools import permutations

# input 단어의 구성만 보고 Palindrome가 될 수 있는지 없는지를 판단하는 함수
def isPalindrome(length, cnt_each_element):

	divide_by_two = [x % 2 for x in cnt_each_element]
	
	if length % 2 == 0:		
		if sum(divide_by_two) != 0:
			return False
		else:
			return True
	else:
		if divide_by_two.count(1) == 1:
			return True
		else:
			return False
		
name = input()
length = len(name)

# 전부 같은 알파벳으로 구성돼있을 때
if len(set(name)) == 1:
	print(name)

# 2개 이상의 알파벳이 단어에 포함될 때
else:
	result = ''

	# 단어 안에 포함된 알파벳 정렬
	consist_of_word = sorted(list(set(name)))
	# 단어의 카운트 수
	cnt_each_element = [name.count(x) for x in consist_of_word]
	# 2로 나눈 단어의 카운트 수
	div_by_two = list(map(lambda x : x % 2, cnt_each_element))
	if isPalindrome(length, cnt_each_element):

		for i in range(len(cnt_each_element)):
			if cnt_each_element[i] == 1:
				continue
			else:
				n = cnt_each_element[i] // 2
				result += consist_of_word[i] * n
	
		center = -1
		for i in range(len(div_by_two)):
			if div_by_two[i] == 1:
				center = i
				break
		if center == -1:
			result += result[::-1]
		else:
			result += consist_of_word[center] + result[::-1]
		print(result)
		
	else:
		print('I\'m Sorry Hansoo')
	
  
		
	