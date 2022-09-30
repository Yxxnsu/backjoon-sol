N, K = map(int, input().split())
multiTab = []
device = list(map(int, input().split()))
takeOut = 0

while device:
	if len(multiTab) != N:
		if device[0] not in multiTab:
			multiTab.append(device.pop(0))
		else:
			device.pop(0)
	else:
		if device[0] in multiTab:
			device.pop(0)
			continue
		else:
			max_dist = 0
			max_idx = 0
			for j in range(len(multiTab)):
				if multiTab[j] not in device:
					max_idx = j
					break
				else:
					if max_dist < device.index(multiTab[j]):
						max_dist = device.index(multiTab[j])
						max_idx = j
					else:
						continue
			multiTab[max_idx] = device.pop(0)
			takeOut += 1
print(takeOut)