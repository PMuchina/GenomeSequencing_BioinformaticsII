def Composition(dna, k):
	kmers = []
	for i in range(0, len(dna) - k + 1):
		kmers.append(dna[i:i+k])
	return kmers

dna = 'CAATCCAAC'
k = 5
kmers = Composition(dna, k)
for kmer in kmers:
	print kmer
