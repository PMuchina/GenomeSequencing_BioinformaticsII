from __future__ import division

file = '../Downloads/file.txt'
count = 0
length = 0
contigs = []
with open(file) as f:
	for line in f:
		line = line.strip('\n')
		temp = list(line)
		if temp[0] == '>':
			temp_ = line.split('_')
			i = int(temp_[3])
			if i >= 1000:
				contigs.append(i)
				length += i
				count += 1
print count, length, 'count, length'
mid = int(length*0.5)
print mid, 'mid'

add = 0
for val in contigs:
	add += val
	if add >= mid:
		print val, add, 'N50, add'
		break



	

