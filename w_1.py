import networkx as nx

def inputFile(file):
	kmers= []
	with open(file) as f:
		for line in f:
			line = line[: -1]
			kmers.append(line)
	return kmers

def Composition(dna, k):
	kmers = []
	for i in range(0, len(dna) - k + 1):
		kmers.append(dna[i:i+k])
	return kmers

def StringSpelledByAGenomePath(kmers):
	string = []
	string.append(kmers[0])
	x = len(kmers[0])
	for i in range(1, len(kmers)):
		string.append(kmers[i][x - 1])
	string = ''.join(string)
	return string

def Prefix(kmer):
	return kmer[0:len(kmer) - 1]

def Suffix(kmer):
	return kmer[1:]

def Overlap(kmers):
	file = open('data.txt', 'w')
	G = nx.DiGraph()
	G.add_nodes_from(kmers)
	for kmer in kmers:
		for kmer_ in kmers:
			if (Suffix(kmer) == Prefix(kmer_)) and (kmer != kmer_):
				G.add_edge(kmer, kmer_)
	for kmer in kmers:
		l = list(G.adj[kmer])
		if len(l) > 0:
			my_list = ','.join(l)
			print kmer,' -> ',my_list
			file.write(str(kmer + ' -> ' + my_list + '\n'))
	file.close()

	return None

#kmers = 'ATGCG GCATG CATGC AGGCA GGCAT GGCAC'
#kmers = kmers.split(' ')
kmers = inputFile('../Downloads/dataset_198_10.txt')
Overlap(kmers)

