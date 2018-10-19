from w_1 import *
from collections import Counter
import random

def inputDict(file):
	d = {}
	keys = []
	values = []
	with open(file) as f:
		for line in f:
			line = line[: -1]
			l = line.split(' -> ')
			keys.append(l[0])
			el = l[1].split(',')
			values.append(el)
	for i in range(0, len(keys)):
		if keys[i] not in d:
			d[keys[i]] = values[i]

	return d

def EulerianCycle(d):
	file = open('EulerianCycle.txt', 'w')
	my_dict = {}
	for key in d:
		if key not in my_dict:
			my_dict[key] = []

	for key in d:
		my_key = key
		break
	stack = []
	stack.append(my_key)
	circuit = []

	while len(stack) > 0:
		vertex = stack[len(stack) - 1]
		edge = random.choice(d[vertex])
		if edge not in my_dict[vertex]:
			stack.append(edge)
			my_dict[vertex].append(edge)
			#print my_dict
		elif Counter(my_dict[vertex]) == Counter(d[vertex]):
				x = stack.pop()
				#print x
				circuit.append(str(x))
	circuit = circuit[:: -1]
	circuit = '->'.join(circuit)
	file.write(circuit)
	file.close()
	return circuit

					
#d = {0 : [3], 1 : [0], 2 : [1, 6], 3 : [2], 4 : [2], 5 : [4], 6 : [5, 8], 7 : [9], 8 : [7], 9 : [6] }
d = inputDict('../Downloads/dataset_203_2.txt')

print EulerianCycle(d)
   