from w_1 import *
from collections import Counter
import random
import itertools
import sys

def inputDict(file):
	d = {}
	keys = []
	values = []
	with open(file) as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[: -1]
			line.strip(" ")
			l = line.split(' -> ')
			keys.append(l[0])
			el = l[1].split(',')
			values.append(el)
	for i in range(0, len(keys)):
		if keys[i] not in d:
			d[keys[i]] = values[i]

	return d

def inputKDmers(file):
	FirstPatterns = []
	SecondPattenrs = []
	with open(file) as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[: -1]
			line.strip(" ")
			l = line.split('|')
			FirstPatterns.append(l[0])
			SecondPattenrs.append(l[1])
	return FirstPatterns,SecondPattenrs

def EulerianCycle(d):
	#file = open('EulerianCycle.txt', 'w')
	my_dict = {}
	for key in d:
		if key not in my_dict:
			my_dict[key] = []

	count = 0

	for key in d:
		my_key = key
		count += 1
		if count == 5:
			break
	stack = []
	stack.append(my_key)
	circuit = []
	
	while len(stack) > 0:
		vertex = stack[len(stack) - 1]
		#print vertex
		edge = random.choice(d[vertex])
		#print edge
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
	#start from a node v, out(v)-in(v) = 1
	#end at a node w, in(v)-out(v) = 1

	virtual_dict = d
	#print virtual_dict
	if end_node not in virtual_dict:
		virtual_dict[end_node] = []
		virtual_dict[end_node].append(start_node)
	elif end_node in virtual_dict:
		virtual_dict[end_node].append(start_node)

	circuit = EulerianCycle(virtual_dict)
	#print circuit
	#print circuit
	circuit = circuit.split('->')
	#circuit = [int(i) for i in circuit]
	l1 = []
	l2 = []
	for i in range(0, len(circuit)):
		if (circuit[i] == end_node) and (circuit[i+1] == start_node):
			l1 = circuit[0: i+1]
			l2 = circuit[i+1: ]
			break
	
	for i in range(1, len(l1)):
		l2.append(l1[i])


	l2 = '->'.join(l2)
	return l2

def StringReconstruction(kmers, k):
	d = DeBruijnGraphFromKmers(kmers)
	#d = inputDictAgain('bruijn.txt')
	path = EulerianPath(d)
	path = path.split('->')
	string = StringSpelledByAGenomePath(path)
	return string


def KUniversalStringProblem(k):
	kstrings = ["".join(seq) for seq in itertools.product("01", repeat=k)]
	#print kstrings, '***********'
	d = DeBruijnGraphFromKmers(kstrings)
	#d = inputDict('bruijn.txt')
	path = EulerianCycle(d)
	#print path
	path = path.split('->')
	string = StringSpelledByAGenomePath(path)
	string = string[0: len(string) - k + 1]
	#print len(string)
	return string

def KDmerCompostition(string, k, d):
	kdmers = []
	for i in range(0, len(string) - 2*k - d + 1):
		l = []
		l.append(string[i:i+k])
		l.append(string[i+k+d:i+d+2*k])
		kdmers.append(l)

	return kdmers

def StringSpelledByPatterns(kmers):
	string = []
	x = len(kmers[0])
	string.append(kmers[0])
	for i in range(1, len(kmers)):
		string.append(kmers[i][x-1])
	string = ''.join(string)
	return string


def StringSpelledByGappedPatterns(FirstPatterns, SecondPatterns, k,d):
    string=''
    PrefixString = StringSpelledByPatterns(FirstPatterns)
    SuffixString = StringSpelledByPatterns(SecondPatterns)
    if SuffixString.startswith(PrefixString[d+k:]):
        string=string + PrefixString[:d+k] + SuffixString
    return string

def DeBruijnGraphFromKDMers(file):
	kdmers = []
	d = {}
	with open(file) as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[: -1]
			line = line.split('|')
			kdmers.append(line)
	nodes = []
	for kdmer in kdmers:
		l = []
		for read in kdmer:
			l.append(Prefix(read))
		nodes.append(l)
		l = []
		for read in kdmer:
			l.append(Suffix(read))
		nodes.append(l)

	for node in nodes:
		node = '|'.join(node)
		if node not in d:
			d[node] = []

	for kdmer in kdmers:
		l = []
		k = []
		for read in kdmer:
			l.append(Suffix(read))
		l = '|'.join(l)
		if l in d:
			for read in kdmer:
				k.append(Prefix(read))
			k = '|'.join(k)
			d[k].append(l)

	return d

def StringReconstructionFromReadPairs(DeBruijDict, k, d):
	path = EulerianPath(DeBruijDict)
	path = path.split('->')
	FirstPatterns = []
	SecondPatterns = []
	for kdmer in path:
		kdmer = kdmer.split('|')
		FirstPatterns.append(kdmer[0])
		SecondPatterns.append(kdmer[1])
	string = StringSpelledByGappedPatterns(FirstPatterns, SecondPatterns, k, d)
	return string

	#for key in d:
	#	print key, ' -> ', d[key]


#FirstPatterns,SecondPatterns = inputKDmers('../Downloads/dataset_204_15.txt')
#k = 50
#d = 200
DeBruijDict = DeBruijnGraphFromKDMers('../Downloads/dataset_204_15.txt')
print StringReconstructionFromReadPairs(DeBruijDict, 50, 200)

#print StringReconstructionFromReadPairs(FirstPatterns, SecondPatterns, k, d)


#l = KDmerCompostition(string, k, d)
#l.sort()
#for i in l:
#	print '(' + str(i[0]) + '|' + str(i[1]) + ')'


#kmers = inputFile('../Downloads/dataset_203_7.txt')
#k = 8 #some random value will work too
#kmers = ['CTTA', 'ACCA', 'TACC', 'GGCT', 'GCTT', 'TTAC']
#print KUniversalStringProblem(k)

#d = {0: [2], 1: [3], 2: [1], 3: [0, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
#kmers = ['CTTA','ACCA','TACC','GGCT','GCTT','TTAC']
#k = 4
#d = inputDict('../Downloads/dataset_203_6.txt')