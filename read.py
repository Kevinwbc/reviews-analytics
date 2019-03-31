data = []
count = 0 #用到計數就想到此列
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #計數用意1次2次
		if count % 100000 == 0:  #如果count的餘數是0
			print(len(data))
