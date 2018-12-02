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

def OverlapUsingDictionary(kmers):
	d = {}
	for kmer in kmers:
		if kmer not in d:
			d[kmer] = []
	for kmer in kmers:
		for kmer_ in kmers:
			if (Suffix(kmer) == Prefix(kmer_)) and (kmer != kmer_):
				d[kmer].append(kmer_)
	for kmer in kmers:
		l = d[kmer]
		if len(l) > 0:
			my_list = ','.join(l)
			print kmer, '->', my_list
	return None

def DeBruijn(dna, k):
	kmers = []
	file = open('hello.txt', 'w')
	t = len(dna)
	for i in range(0, t - k + 1):
		kmers.append(dna[i:i+k])

	d = {}
	for kmer in kmers:
		if Prefix(kmer) not in d:
			d[Prefix(kmer)] = []

	for kmer in kmers:
		d[Prefix(kmer)].append(Suffix(kmer))

	for key in d:
		l = d[key]
		l.sort()
		if len(l) > 0:
			my_list = ','.join(l)
			print key, '->', my_list
			file.write(str(key + ' -> ' + my_list + '\n'))
	file.close()
	return None

def DeBruijnGraphFromKmers(kmers):
	#file = open('bruijn.txt', 'w')
	d = {}
	for kmer in kmers:
		if Prefix(kmer) not in d:
			d[Prefix(kmer)] = []

	for kmer in kmers:
		d[Prefix(kmer)].append(Suffix(kmer))

	#for key in d:
	#	l = d[key]
	#	l.sort()
	#	if len(l) > 0:
	#		my_list = ','.join(l)
	##		#print key, '->', my_list
	#		file.write(str(key + ' -> ' + my_list + '\n'))
	#file.close()
	return d
	

#dna = 'CCACCAAGCTCAAAACTTGACCGCCTAAGAGCACCATTTACTGCTTCGTATGTTAGGAAGATGTCATTACGACGGGAGTCTATGTCCCGCTCACGCATCTGGGTGAGGATGAATGTAGGGGAACCCCCCGGCTTTTCTACCGGACGGAAGTTGGTAGCGACCGTGCCTGCAAAATGTACTGATGGCGTTGGCCAGACATTAACCCTACTACCCCACCCGCTCATTGTCACGTCTGCCTTCGTCAAGAGTCGGTGACCCCTAACCGGACGGTGGAGGCATGGTTATTTCTTGCTTGGGTTGGTTGATGGTAAAAGCAGCTGCAAGCAGTATCGTGTCGGAAGCTTAAAGTTCACGCAAAAGTCCGTCCATTACCGGTACTGATGGAGTGAACGAGACCGAATACATGCTCACGCATCTTAGATGAATACAGCAGAGCATGCTACACGGTCGGTGGAGAGCTTGCCAGAGTTAATACGAGCGATGGGGAGTTTGGATCCTACGTGCGATAGCCTAAACTTTGCTTCCTCAGCATTGACTCATTAACGCCTAGCTATTCAGCATGCTAGATTGCATGCTGATATGTCTGATTTTCGTTTGCACTCATGCAGTAGTGGTCAGCTCCCACGGCGTATCTCCGCATTCACACCACTTTCTTCCTACGGACCGTATTACAGTCGGTAAGCGTGATGCGAGAACGTTCAGCGGACACGGGCTATTGACTTTGTCACATCTTGTCTTTTGCGTTACGCGTGCGTTAGCTACAGTCGAACAGTCCAACGCCCCTGTTACGGTATGTTAGCTCTTGTAGATTACGTCCAGCGAACAATGCATACCTGGTCGCGGCTCCGGGGCGCCAGAAACATTCCAGATCTATAGTTACACCTCCTTCCAGATACTAGAGAAGTCTTTACTCTATTGATAAGTACCCGACGGACCAGTAAGGATTTACGTGGTGGATGCGCGGAGGGGGTGTGCGCAGTTACACAGCGGGCCTAGGTTGGGCTTTGTATAAGGCGCGCATCTAAGGTACCTCGGGGGTCGACCGGGATTCTACAGTCGTAACGGGGCGTTAGTCTCACACGGATTAAATCTTTACGTCAAAGCGCATAGGAGGGCGGTATGAGCAATACCAGCCCGAGTCGAGTTCTTTATAATGCTTATGTGGCAACGTGATAGTGCTCATGGGATAATGGGCTGAGCCCAGGCACCTGTCCGACCTCTGATGGGGGTAAAGCACTCGATTTTTGGTTATGTAGTGCGAGTAGGTTTCTAGTCACCCTAAGGACGGCACGCAATCATCTTCTTCCCCCCTGTCGTATGATTGTGAGTTGGGCATTCAAGTCGCACTGCCAGGGGTCATTCAGTGCCGGCGTCTGGGTTAATTCCTCGGTAGGCGGTAGCGGTGCTAATGAAGAGATTGATTTGGCCTGCAAGCCTTCTTGCTTCATTCTAGACAGGACTAGCTAGTGTATCCCCGCTGAGAGCAACCAGCCTGCCACCGACACTAGGTCAAACTAAAAGCTGAGCCCTTCGGAACAGCGCCTTCTGCCCATTCCAACTGCGGCAGCCTGTCTAACTGCGGCCATTGTCCATGCAGGTCGAGTATTGGTTTAGGTCACGCCACTAGACAGCTTCATATCAAATTGCTGAAATGAGAAAGACGCGGTGTTGGTCGGGTAAGGGGGTTTGACCGCTGACCCCGGACGGAGCAGAGACTTATTTAACGTTACATGCTCGAATATTTTTACAGGATTTGGTATCAGTCGTGACCCGGGTGGCTAAGGCTCAGCATGCCTCTTCCTTCAGTGTACCATGATGAAGATTCATCTAAAGACCCTCTGACGATAAGTCTTCTCTAACACCGTTGGAATCGGATCGTGACAGATCAACCTTCGGGTCGCAAAGCGCCGTTTGCATGGTTAAGTAAGTGGCAATAGTCCATGGTTGAGAGTTCCTGCTAAACCTACCCCGTCGCAGATGCTCTACACTGCAACAATCCT'
#k = 12
#DeBruin(dna, k)

#kmers = 'GCGA CAAG AAGA GCCG ACAA AGTA TAGG AGTA ACGT AGCC TTCG AGTT AGTA CGTA GCGC GCGA GGTC GCAT AAGC TAGA ACAG TAGA TCCT CCCC GCGC ATCC AGTA AAGA GCGA CGTA'


#kmers = inputFile('../Downloads/dataset_200_8.txt')



#kmers = 'GAGG CAGG GGGG GGGA CAGG AGGG GGAG'
#kmers = kmers.split(' ')
#DeBruijnGraphFromKmers(kmers)

#DeBruijn(dna, k)

