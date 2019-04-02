data = []
count = 0 #用到計數就想到此列
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  #計數用意1次2次
		if count % 100000 == 0:  #如果count的餘數是0
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:       #求每一筆的資料於data內
	sum_len = sum_len + len(d)  #len(d)為每一筆資料長度
print('留言的平均長度為: ', sum_len / len(data), '個字') #留言的平均長度


new = []  #清單
for d in data:  #d是字串data是清單
	if len(d) < 100:
		new.append(d)   #把者些d資料裝進new清單內
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
