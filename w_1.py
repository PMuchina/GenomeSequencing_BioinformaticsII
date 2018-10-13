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

kmers = inputFile('../Downloads/dataset_198_3.txt')
print StringSpelledByAGenomePath(kmers)
