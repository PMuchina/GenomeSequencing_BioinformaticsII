from w_1 import *
from collections import Counter
import random
import itertools

def inputDict(file):
	d = {}
	keys = []
	values = []
	with open(file) as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[: -1]
			#print line, 'line[::-1]********'
			l = line.split(' -> ')
			#print l, 'line.split()********'
			keys.append(l[0])
			#print keys, 'keys *********'
			el = l[1].split(',')
			#el = [int(i) for i in el]
			#print el, 'el ********'
			values.append(el)
	for i in range(0, len(keys)):
		if keys[i] not in d:
			d[keys[i]] = values[i]
			#print keys[i], d[keys[i]], 'keys[i] --> values[i]*******'

	return d


def EulerianCycle(d):
	#file = open('EulerianCycle.txt', 'w')
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
	#file.write(circuit)
	#file.close()
	return circuit

def EulerianPath(d):
	degree_dict = {}
	#d[key] = [outdegree, indegree]
	for key in d:
		if key not in degree_dict:
			degree_dict[key] = []
		for x in d[key]:
			if x not in degree_dict:
				degree_dict[x] = []
	#outdegrees
	for key in degree_dict:
		if (key in degree_dict) and (key not in d):
			degree_dict[key].append(0)
		else:
			degree_dict[key].append(len(d[key]))
	#indegrees
	for key in degree_dict:
		count_in_key = 0
		for key_ in d:
			l = d[key_]
			if key in l:
				count_in_key += 1
		degree_dict[key].append(count_in_key)

	#finding start and end node
	for key in degree_dict:
		l = degree_dict[key]
		if (l[0] - l[1] == 1):
			start_node = key
			break
	for key in degree_dict:
		l = degree_dict[key]
		if (l[1] - l[0] == 1):
			end_node = key
			break
	#print start_node, end_node

	virtual_dict = d
	#print virtual_dict
	if end_node not in virtual_dict:
		virtual_dict[end_node] = []
		virtual_dict[end_node].append(start_node)
	elif end_node in virtual_dict:
		virtual_dict[end_node].append(start_node)
	#print virtual_dict

	circuit = EulerianCycle(virtual_dict)
	#print circuit
	circuit = circuit.split('->')
	#circuit = [int(i) for i in circuit]
	#print circuit
	l1 = []
	l2 = []
	for i in range(0, len(circuit)):
		if (circuit[i] == str(end_node)) and (circuit[i+1] == str(start_node)):
			l1 = circuit[0: i+1]
			l2 = circuit[i+1: ]
			break
	#print l1,'###############'
	#print l2, '&&&&&&&&&&&&&&&'
	for i in range(1, len(l1)):
		l2.append(l1[i])


	l2 = '->'.join(l2)
	return l2

def StringReconstruction(kmers, k):
	DeBruijnGraphFromKmers(kmers)
	d = inputDict('bruijn.txt')
	path = EulerianPath(d)
	path = path.split('->')
	string = StringSpelledByAGenomePath(path)
	return string


def KUniversalStringProblem(k):
	kstrings = ["".join(seq) for seq in itertools.product("01", repeat=k)]
	#print kstrings, '***********'
	DeBruijnGraphFromKmers(kstrings)
	d = inputDict('bruijn.txt')
	path = EulerianCycle(d)
	#print path
	path = path.split('->')
	string = StringSpelledByAGenomePath(path)
	string = string[0: len(string) - k + 1]
	print len(string)
	return string

def KDmerCompostition(string, k, d):
	kdmers = []
	for i in range(0, len(string) - 2*k + 1 - d):
		l = []
		l.append(string[i:i+k])
		l.append(string[i+k+d:i+d+2*k])
		kdmers.append(l)

	return kdmers


k = 3
d = 2
string = 'TAATGCCATGGGATGTT'
l = KDmerCompostition(string, k, d)
l.sort()
for i in l:
	print '(' + str(i[0]) + '|' + str(i[1]) + ')'


#kmers = inputFile('../Downloads/dataset_203_7.txt')
#k = 8 #some random value will work too
#kmers = ['CTTA', 'ACCA', 'TACC', 'GGCT', 'GCTT', 'TTAC']
#print KUniversalStringProblem(k)

#d = {0: [2], 1: [3], 2: [1], 3: [0, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
#d = inputDict('../Downloads/dataset_203_6.txt')
#print EulerianPath(d)
   