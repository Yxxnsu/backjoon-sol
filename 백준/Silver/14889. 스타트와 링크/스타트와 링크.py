from itertools import combinations

people = int(input())
p_list = [x for x in range(people)]
ability = [list(map(int, input().split())) for _ in range(people)]
combi = list(combinations(p_list,people // 2))

start_team = combi[:len(combi) // 2]
link_team = combi[len(combi) // 2:]

min = 1e9

for i in range(len(start_team)):
	s_team = start_team[len(start_team) - i - 1]
	l_team = link_team[i]
	s_sum = l_sum = 0	
	for j in range(len(s_team)):
		for k in range(j+1, len(s_team)):
			n_s, m_s = s_team[j], s_team[k]
			n_l, m_l = l_team[j], l_team[k]
			s_sum += ability[n_s][m_s] + ability[m_s][n_s]
			l_sum += ability[n_l][m_l] + ability[m_l][n_l]
	if min > abs(s_sum - l_sum):
		min = abs(s_sum - l_sum)
print(min)