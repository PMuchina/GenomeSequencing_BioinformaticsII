
def reverseComplement(string):
	myStr = []
	for i in range(0, len(string)):
		if string[i] == 'A':
			myStr.append('T')
		elif string[i] == 'T':
			myStr.append('A')
		elif string[i] == 'G':
			myStr.append('C')
		elif string[i] == 'C':
			myStr.append('G')

	myStr = myStr[::-1]
	myStr = "".join(myStr)
	return myStr

def CodonDictionary():
	file = '../Downloads/RNA_codon_table_1.txt'
	d = {}
	with open(file) as f:
		for line in f:
			line = line.strip('\n')
			l = line.split(' ')
			if l[0] not in d:
				d[l[0]] = l[1]

	return d

def IntergerMassDictionary():
	file = '../Downloads/integer_mass_table.txt'
	d ={}
	with open(file) as f:
		for line in f:
			line = line.strip('\n')
			l = line.split(' ')
			if l[0] not in d:
				d[l[0]] = l[1]

	return d


def ProteinTranslation(rna):
	pattern = []
	d = CodonDictionary()
	rnaCodons = [rna[i:i+3] for i in range(0, len(rna), 3)]
	for codon in rnaCodons:
		pattern.append(d[codon])
	pattern = ''.join(pattern)
	return pattern

def SubstringEncodingAminoAcid(rna, aminoAcid):
	substrings = []
	substringLen = len(aminoAcid)*3
	for i in range(0, len(rna) - substringLen + 1):
		substrings.append(rna[i:i+substringLen])
	encoders = []
	for sub in substrings:
		reverse = reverseComplement(sub)
		reverseTranslated = reverse.replace('T','U')
		translated = sub.replace('T','U')
		if ProteinTranslation(translated) == aminoAcid or ProteinTranslation(reverseTranslated) == aminoAcid:
			encoders.append(sub)
	return encoders


def NumberOfSubpeptides(n):
	return n*(n-1)

def LinearSpectrum(peptide, integer_mass_dict):
	peptide = list(peptide)
	PrefixMass = [0 for i in range(len(peptide) + 1)]
	for i in range(1, len(peptide) + 1):
		PrefixMass[i] = PrefixMass[i - 1] + int(integer_mass_dict[peptide[i - 1]])

	LinearSpectrum = []
	LinearSpectrum.append(0)

	for i in range(0, len(PrefixMass) - 1):
		for j in range(i + 1, len(PrefixMass)):
			LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])

	LinearSpectrum.sort()

	return LinearSpectrum





#n = 24460
#print NumberOfSubpeptides(n)

#rna = 'GTTACCGTAGCCTCGTTCGGTCTTTATGATTAACAAAAACTTCGTGACCCGAGGGGCCGTCCACGCTCGTGTATTTTCGTGTACTGTCACCCCCACGGCAACATTGTTGAGATTAAAATACGGAGCATCTGAGCACGGGTAGTGAGATCTATTAGCAATCGATAGTATCTCGCGCGAAGGTTGCGATTTCTCTTTAGCCGAAGTCGCCTACGTTCCGGTTGAACTAGATGTGAAGCCAGGGTGGACCAGGTTCATACAGGGGAGGCGAGATAAATCGAAAAATTAGTCCCCAAGAGCGAGTACACCAAGTTCCTGAGTATCCAAGAACTGACCGCTCGATTCACCGAACACGAATGCTAACTTTTTATGGCGTCATTTCCGGGGGTGATTTCTACACATGGTAAACCTTCACACCATAGATGAGTCGAGTACGTCAACGTTTGGTGCGCGCGTGACGCACAGACGGTTCGGAATAAACTCAATGCCAGTCCCTATGGAAGGGTAACAACTCGTGAGGGCAGGAGATATCTGGTTCTCATAAAATATTACGGCCTCGATACGTAATCAGGCGAGTGATCTCGGGTGTGGTCACCGCATAATAGCAGTTCTGCATTATCCGCGAATTTTTCGGTTGATAGTGCTGGGTACGAAATGACCTGGCAGAATCGTAACTCACCGCTGTGGAAGGACTGGAACCCTGCACTATGGGATAGCCGCGGAGCCCTAGCTCGTTTGTCCAACCAGGTCATACAGCAGTCATCTGCCCTTCCGTATTCATAAGGCCTCTAGCGCATGGCGCTAGCGCAGCTTACCGGACTTTAGGCATAAACAATCGAAAGAACTTAGTTTCGTTACGACGATCCGCGATCGTACGGGATTTTGTCATAGATGGTAGGAAGTCCCGCACTCATGGCAGTTAATGATCGACCGATCGTCGTGGACGGACGGCACGGCTGGTCTGCCTTGATCGGATCAACTCTATGCCCGTTCCAATGCGGTTTCGAGCCAACCGAACAGTGAGGGAACTTGGCCGTGCAACCGTCAGTGATGGATCCAGCAAGCATAATCACCCTTGTGAGCTGGAAGCCAGTTCGGGCCTCGCTGGAAGGTCATACTCCGGCCCAGGTACAATTTGGCTCGATTCACTACGGTACTCGTTCGTGAGCTCTAGACCTAAGAACTCAGCTGATCTCCACGTCCTCCATACCGCGAAGCGCGTGATAGGCCTGAGAAGCAGTAGCGCCACTCTTAAGTGTGCGTAAATTGCTATTGGCACCCGTCAGCGAATAAGGTAATATGTCGGACCCTGAAACGGAGCTTTAACGACTTCTGGTCGATGTTGGTTGTGAAACTCTATTTTTTCTTGGTTCAGCTGAAACCAAACCTAGCCGGGTACCGTCAGGCGGCACTTGACTACTTGTACGCGATACCTTGGGGTCAGGTTACAGCAGTGTAAGGACCCCGCGAAGTGCAGGTGGAGGAGCCCAAGTTACCGCTCGCGACCATAAGATGGGCGTAGCGAACCCATCTATGATAGCTCCCGCGATTTCAATTTGTGCTCTTTATGAGCCTTACCCAGTCCACCGCAGGGGCTTACCGAGTTCTCGCAGATAGGCAAAATAATTGGGGGGCAATTAATTTTACGATAAATACATGCCTTCGCGGAGTCTGTGGGATCGCAGCAATGCTCACTACACCAGTCTTGCCTGCCTGGGCGAGAATGCGTGGGTGACGATATATTGAGCACCACACTATCGAGCATCGCCGCGATTTTGCCGTGTGGCGGACTGCTCCGAGATCGGGACCGGAAAAGTGGTTGTCCTCTAGATGTCGCACCTACGAGCGCCGCATTGGCACCGGCATACTGTTAATAGTGCATTATGGAAGAATAAGCAGCTATACTCCAGACTTGTGCACTTCCTATAGGGAGTATTTATGGCCGGACCGTAACCCATAGGGACCGGCATACTATTGATATCTCAACTAAACTTGCCACCTAAACCCCCACAAGGCTACATTAAAAACATGGGGCCACAGATGTATTGCATTATGTTTGCAGCAGTAACAGTGGGCGTTCTGGCGCAGTCCAGGTAACTAATGATAGTCATTAGCGGATAGTCACACAGCATATACCTCGACTGCTAAAGGTTACCCTACCGTTGTTTTAAATATCGGACCGGAACCTGCTGTGGTAAAACGCCCAATTACAGCTTAAGTCAATAGGGCATTAATAGTATGCCCGTACCAATGGCGCAACGGTGGGCGTGTGCGGTTAGCAAGGTATCGTTGCAGCTTCTTCAGATCTGATTGGAGTGTCGTCCCCAAAAAATTCATCCGTTTGGGCGATGACAACGGTCCAACAAAGCTTCTCGCGTCCGTAAGAGATTGGATTCAACTCGAGGAACTTTTGACCTAAGATGACCGCACCCAGTACCAATAAAGTGGATCAGTCCTAGTTACTACGGATAAGTGGGGACCACCCAATCAGTACGGACACTTCGACAAGTATAAGAGCACATGCCATGTTACCGATGTGATCCTATAGCGGGCTTAACCCTGTGGCGCCTACTATAAGCGGCATTCTCCGAGGTGCCATGATTTGGATTACCGGCGGTGCGCGGATCTTGGCCAACGGCAGCACGCAAAATACACCTTCCCGTGAAATGCAGGGATACTCATATACGGAGAACACGCATCCCGCACGATATATCTCGGTAGAAAGCAATGGGGCTGGGCAGTAAGCCCGATATTTATCGCACCTCCCCAAGGCAAGTCTAGTCATTCAAATCATACCGCCGTTTACTCTCCACACGCTGTACGGTTTATACCATGATGGTCGGTATGATACAGGGTCGCCTTCTGCTATTACGAACAGCGCGTAGTAATTTTGGAAGATAAATGCGCACAAATGAGATTTCTTGAGCTGGAACCTGGTCCCAAGGTCAGTGCCCCACTGGTGATCATGTATTAGTGAGGAGCCTATTTTCGCACGAGTCACAAGTGGTGACCTAGTGGTCCCTCGCGTTGTTACGCTGGTATCTCAGAGGAAATCCCTCACATTGCTACCGGGGGTGTGCTGCTCTGGCCCCGTGAGTGGCATCAATTCCATGCCCGTACCAATGTTTCGCACCGATCTCATGGGGACTGGCATAGAATTAATTTTCGGCTTTGGGCATTAGAAGCCGATGCAGACATTAACTAAAAAGACGATCCAGCAAGAGTTGGGTTGATACAGATACTAATTCCATAAGAGAAGACGTATCCCCCTTTCGCCAGCGTCTGCAAACTAATAGTCATCACTTGGACCAGTGAGTAGCCCAGGTAGTATTTTACGAGAGTTCGGGGAAAGGTCCTTCTGACACGTCCAGACTCAGTTTTCGCATAAGGTTCAAATCTATGGGTTTCCCTGACTGCTAGGGCCAGGGGTGACTCACGCGTCTTTCCTGATCCTCAGCCCTTTACCCTTCCAGACTACTGAATGACATCGGTACTGGCATTGAGTTAATAGGCGGGTCATACGTATGAGCTCCTTCCCTGGATAGCTATGATCTCTGACGGTCCGACAGGTAGAAGTGATGGGGGGCCCTGCCGCTTCGATGAAGCCAGTAGCTCGGCGGAAGACAATCACCCGTAAGTTGTCTTCCCTGATCGCGGTTCTGTCACCCCGGCCACTGCGGCTAGACGCAATGAGAAACCGCTCTGTCCCAGTTCGATAGCAATAAACAAATACGAACAGCGCACCGGGATTATGGCCCGCGCGCCTTCGGCACCTATAACATCGAGTGAATGCATGGACTACAGGCCTGGGCACCCTATTTGAGACCATCGACGTTTAAGTGAGAGGTGCCAAATTCATCCGGAGCGTGGCTTCCCGGAACTAACCCACAGTCGGCTAATTGAAATGAGATCGTCGACCTGTCTATGACTTAGACATGGCCCTCCAAGGGCCCCGATCTCCATCGCACACCACCTCGAAATTTGTTGGAATTAATTCTATGCCAGTTCCCATGTTTACCGCTTGTGTCCAGCTGATGCCGACTCCCCGTGGTCCAGTGTAATCTATGTGCCCACGAGACCTATAAGTGTCCTTGTACACTAATCCGAGTGCGATTATCGACACACAGCAGGCGGGAGGGGCTGGAAAGCATCTCCTTTCGGTCATTTAGTGAGTATCGTCGTTCATACTGGCTTCCGGTCCATGGTCCTCGCTATGCGAGGGCCTTCAACTATTCAGGTAACCCTATCGCCGCAGAGAAAGTGCAATGCGAACCAAACGATTGAACTATCTAACCTAGGCGGTGAGAACCGCCAGGGTTCATGGCGGATCAGCTAGTTCACCAACTCGCTTGACTCATTAGTCGGCTGCGGACTGTCTAGTACACCCGAAACCGCCATTGGTACAGGCATGGAGTTAATTGTGAGGAAGTCCGAATTAGAAGCGTATGTTGCGCCTGCATATGTCACCACTCCAAACTGTTTTGTTCAGTAACGGTTATGTTACTTGCCAGTACGCTGCGCGGTGACTTTAAACGGATCCTGCGTCAAGGGTTAGGAGTACTTCTGTACGATAACCCATAAACAGATTAGTGGAAGCATCCTGTTTAAGATTCCGCGGTGTTCGAACCGCCCGATGCGTCGAGGGTTCAGGTACACGCCAATAGCCCCATGGGCCATATGCTCGAAACTATTTCGTGTGTTGGTGTGCCAGTGATAACGTTATACAGCCAGTGTCTAAAGACCACGTTTCATTCCCCCGGCGGCCTCTGCGTTGCGAGCCCATAGGATCCTAGTTGCGCGACTCGTAGCCCAAGCGCGTGCTACTCGCTATGACTCCGTGATTCAATTTAATGCCATAGGAGACTGCAGGCACATCCTCGCTGAATCTGATCTCCGACCTGAAGGACGATTCTATGCTCACCTTGTCGTCTATAAGTTGGTGCATTAGTCTAACCGTCGCTAAATCGCTGCGGGACGCTTCCTCTCGCATAGGCACGCGCTCACTCTGTAACCATGGTATTTGATGCTCTAGCGTACATCAATAGCATGCCGGTGCCCATGGAAATGCATACGTCGAGCCGCATCGGGGTACGGAGCCTACACGTTGCTGCGCCCCGCGTCGTATTTACCACTGGCCCGAGTCGAAGGATTGTTTTAGCTGCGACAAGGATGGTCAGGTGGACATTGGCACGGGCATGGAGTTAATTTCCCTCTCACTTTTCACACGAAGTGGACAGCCAACGGGTTCATTGGGACCGGCATGCTGTTAATCGTTGCTTCATGGTTCTGATCATGACCCTTTCGGCTCTAGCCTACAGTCAAAGGCATGTGGTGCGTCACTCAGATTCACATTAGGATTGTTTTTTAAGCAGGATTCTAGTCTCGATTTTTGAGCAGCATTTAGTGTTCTGTGGCTTGCGGGCCAAGAATAGTTAAACTAGTAACAATGGGCAGGTGGAGGGAAGCGTATCTATCGTAGGGAATGTCGTATCCGAGTTGTACCTATCTGAGCCTCTCTCCCAATCCTAACGGCTGGTAACAAACCGCCAACAAGCGGTCTCAGTTTCTATGACTTCTTCAGCCCTGCAGTGTCTAAATTCTTCGGCTTGGTCATGCCAGCCTCTCCTGTGCGCGGTCAAAGCTCCTTACCCGAATATCGCAGACCGGTGTCCTACAGAGTTCAGGATAGTGTGTTACTGATTATCAGATAGGCGGCACCACTGACCGCAGGCTACGACGCGATAAGAAGAAGATGGCGGGGCCCTGCATATCGGCCCTGGCATGATTATCTGATACCCGTAGGTTCCTTCTAGCGTAGGTAAATTACTTCATACACGACCCTGTTTTTAGCACCACCCGCTTGATTGCGGGCGATCAATTCAATGCCGGTCCCTATGAGTTAATGTTTTATGTTCCCCATGTAGGGCAGGGATGTGCAATCACTGGCATAAGAGCAATGTCTTTCCCATAATCTCATATCCCTAACTACAGACTGCAAACATTAAGGGACAATTACCCTTATAAGACAGGTGATCTGATCGATCCGGCTTCAGATATGGTATGATGGTCTGCGTATTATTGCTGCCAACCCGCCAAATACAGTTCTCCCTCACGGGGACGGCGGGTTTGGGATAATGATTGAGTCACAGAAGTATTCGCTTTGCCTGCTTAAAACACCCGAGTTCGACACTGCTACTTTGACAACTCTGGGAATTGAAGCGTACGGCACGTACAGCCCCAATTTAGCGTCGTACATACGGTCCTTACATAGATATTCTGGGTACTCCAAACGGTCCGATGCCGCAAAAACATTAGCGGGCGCTCCGGTAATGTTCCGAAACATAGGCCTGGTAGACGTGCTCAAGCGTCACGCATTGGTACGGGCATCGAATTTATATTCTAAGCGCCCTAGGGCACATTAAAGCCCAATTGATAGATGCACGCGTAAGACATCCCAGCCCAGTTGCGCCAACGGACGCTGACTGAATATTGTAAAGTGCCTACAAACTATACTGCTTGCCAACTGTCTTCTAAGATTTAGGGAAGAAAGAGGATAGGGGAGTCTATAACCGGAGGATACATATAAACTCTATGCCGGTACCAATGTCAGAATATTTGCCCCGTGTGTTTGGATATTAGGTTTTCGTCCATGGTGAGCTGCGGTGTATTAGGGGGGCATCCGCACCGGCATGAAGTGTCCTCATACAAGACAAGCTGATCCAGACTACCCCATGCGTGTCTATTACGCTGGAGCAGCACAGCCCCTAATCCGTGGGGTATGTGACGTCTCCTGTAAAGTTCCCGCTAAGTGGACTCGTTAGTGCATCAGACGCGAGTGCCCGTACCACCGAAGCCTGACTCCCTTGGCTCTTTCACCTTTCCCAATTGGAGTTTGTTGTCCGATAAATACAAAATCAGGCCTATTTGTCGAATTAGAAAGGGGCAGAAAATCCATGAGGGTTTGCGGTACCCCGCTACGACCAATAAAGGTAGGTAGGGCCTCGGCGATCGTAGATTAAACTTGGTGGGTGTGTCGACAGTCCGCTCTGATCTGGCCGTAACAGATAAGCTGTGGGATGCACGCAGGACAGGGGCTGCGAGGTCACACCGATGCGATCACCGTCTTGGGCGTGTGGAGGAGCATAAAGGATTGGGAACAGAGGGTCTTGGGCAGAAATCTGTCATCGCCAGCCCAGAAGGTCGAATGTTCTCCGCGACAGGTGCCGTGAATGAGATGGGACTGGAATTCAGATTATGCGCCTGGTAAGAACTCACTAAAATTCGAAAATGTTTCCAGTATTACCTCGGACCAATGTGCTGACTAACGGCAGTGGTGCGAACTCTGAACGTCAGTAGTGCTCCAGGATCTCCACAACGACATCACGATCCATCACAGGGGCTCATGTCGGTTGTGATACAGTGACCAAACATACCTCCAGGGCGTGCCACCGGTGGACGCTCGCTGACGTAGGGTGGGTAGGTTAATCGCTCACGTATCCTCAGATTAATACGCCATCAGGCCGCTCTCTTTGTCATAAATTCGATGCCGGTGCCGATGCGATGCTCGTAGCTACTGGAGTCGGACGTACATATTGTATGCTATTGGTGGAGGTACCACTAGCAGTGCGGAATAGCACTAAGGACGAAGATATAAGCGATAATGCATACCTCCACGGTGACGCTCAATCCTGGTTCTATAAAACGTTGTGGATCCAAATATGGCAAGAAGGCTAATAAGTAAGGGCGACTCGCCATCTTATCAACTCCATGCCCGTCCCTATGCCCTGGTAGGCTGTATCATAGCCCCCCCGAAAACAACAGAGAATTTTCGGATGCAAAAACTAGTTTGCCTGACCGAATCCGTCCGAAGGCGGTCTGGGACGCCGCGACCTGTTTACAATGTGTCCAAGAGCCTAGGGATTGCGCACCGAGTGCGTGTTTCACGATCTCGAGGTCGAGCGTTTGTGGATCAACAGTATGCCTGTGCCGATGAGAGGAAATTGTCTATTGGCGAACCACATTCCCAACAATCTGTGCGTGGATGCTCATGGGTATGGTGACCGGGGTTGTCGCTGTATAAGCGCCTGTGACGGTTCCTGCTAGCTAGTAGTGGCTACAACCTCGCATGCTGTCTTGGAGGCCTGGGGGATCACCTCGCAAG'
#aminoAcid = 'INSMPVPM'
#encoders = SubstringEncodingAmninoAcid(rna, aminoAcid)
#for encoder in encoders:
#	print encoder

#rna = 'AUGUAUGGCAAUGCUAUAUGCUUACUGUGCAACCCCUUACACGCCUUAGUACUCAGGGUGCUAUGCGCCCAGUCGGGCGAGCGCUAUUACUAUGGUAUCUUUAAGAAUCACUAUCCAAUGCAUUUUACCUUCUUAAAGACCGGGACCUGUCCGACGUACAAUCAAGUCUCAAGCACCCGUAUUUCAAAAGAAACAAUAGCACUUGUCUGGCCCACUACGCGGAAGCAACAUCGAACCGAUCUUAGAUCUUUUCUCACUAAAGUCGUAUACAGGGCGUAUCAUCAUCGGGCCUCUGCUGUCACUUGCAGUCUACUUAAGAUGUUGGAGCCAGUGGUCCAGGCCGCCGAGGUCUUCCUACCUUGGAAAGGUCCUAUUUUCGCACCGGUGGAGAGUGGAACUUUGUCUAACUUCUUCUUAACGCAGCUUUGGAUUUGUGGCCGCUUACAACGUAAAUUGGUCAUAGAGAUGUACGCUGAAAGAGGAUUAAUCCGGAAGGCCCCAACCAGCCUCUCUCGCAGAUUAAAAUGUGAUAGUGACUCAUUCUACCCAGGUUUUAUGAAAUUCGACACUAAGGUUGCCGAUCGGAAUCGGCCUAAGAAGGAAGAGACGAUCUCCACCACCCUCGACGGCGUGUCGUCUUUGCCAGUCUCCUCCCCAAUCAUAGAUAUCUAUGGCAGAAGCGUCAAGGUUUUGAACUGUGUGACCAAGCAUAUCGUUAUCGGGCGAAAGACUCUAAAGCGCGUUAAGUAUGCAAGACAACUUUCAUGCGUCCUGGUAUGCUGCGCAUCGGAGCUGUUAGACUAUAUUAACCGUACCUAUUCAAUACCGCAAAUCGGUGGGACCAAGGGGCGAAAGAGCGGACUUAGUGGUUAUGCUGUUAAUAUUGGUGCUAACACUACCACCGCGGAUCUGUUCACUUCUGUGAAGACGCCAGAGCUAUUUAGGGAGUGGGUUAACACAAGGAAAACUUACAUCCUUCCCCGGCAUUUUUUACGUAGGAGGUGGUUAGCUCAACGCCUCCCGUGUGGACAUAUCUCUAGUAAAUGUAAGACCGGGGGGCAUCUUCUAGGUUCCAACUCGGUCCCUUGGCAUCUGAAAGCCAGCCACGGCAGCCGCGACAGAAUUAGUCUUCUCUCUAGGUUCGCCGUUCGGUACAAAAUGCUGGGUAGGGUCAGGGAGCCCUACUCGCUACUUCUCCGAGUGCUUUUUCCCCCUAAGAUUCGAACUGUGAUCCUCCGGCAAUGCUCUGUGAAGGUCUUGUCCGUCGGCAGGUUCACACGUAAGGCAACGUUAUCGGCCCGGAAUGAUCCGGUGACCCUGAUCGCGCCCCUAAAACAGCAUGUAGCCUCUAAUAUCACCGUUUCCUACUCCAUGUUGAGGAGAUCUGAUCAGAAAGCCAUUCGCUGCGCCCGCGCGCAGUGCCCCCGCCGCGAACUAUGCGAUAGGUUGAACGCAUUCCCAAGGCCCUCCUCCCUAUGGCCUUAUACGCAGGCCUUGACAUAUCAGGUCCCUGUCGCAGAGCGAUACUUGUCCCACAGCUUGUGGACCGUUGGGGAUAAAUUGUAUAAAACAAUCACAUUAGUGUUAAACUGGGCCGCAUUAUCGUAUCACCUCCUCAGGGGUCAUUAUGCUGAUACUGCUUGGUUACCUAGGAUCUGUGUUCGCACCGGGGCCUUCCACUAUGGACCGCUCAGGGGUCAUCAUUAUUGCUCCCCGAAGUUACAACGAGCCCGCGUUGGACUGUGGAUUACUGACUACCCCAGAUCUUCUAACCUAAAGAGUACCCAUCGAUACCACCGGGAAGUUUUUAUGUCUAGAGCGUUGGGACACUCCAAACGGCCCGGGCGACCUCUGAGCCCAAGAAUGCUAAUCGGCGAUUAUGAAUCACCCUGCUAUUGCAGAGGCUGCAGAGGUAUCAAAUCCUAUAGCGGGAUAAAACCGACUGUCCAGCUAGCUAGAUGUGGCGCGCGGCGAGAGAUACCUUCGAUGCCUAUCUGCCCAGCACCAUUGCCACGGUUUAUGUACAAUGUCACCAUAGCUGCGGUAGCCUCUUCUACCAAUCGGUAUGUAUGCAUCAAUAUAGUGGCUCCGAGUGUUCGAGAGGGGGACGGGAGGAUCCUGUUACAGCUUAUCCGACAGACACCUUCUAAUGGUCCCAGAAGUAUAUCUCGUAACGAAGUAGCGCGGCAUUUGUGGGACGCUCCACCGCACUCACACAUUUUGGAUAAAACAGCAUACUUAUCAGCUUCACCCGGUAGCGACCGUAAUACCGGACGUUUUCUAUCCUUUGUCCCAGUCUACGCUUACCCAGCGACCGGGAUCCAAGCAAAGCUAUGUUGCUUGAAACCAAUGAUUCUACACUGCUUCCUAGGCAAGAUGGUUGAGGAUUCACAAGGGUACUACGGCUUUCUGCGGACGGCACUCAUGCGUGGUAACAGGAGGUUCAGUAUUCCGAGGUACCACACGGCGCUUAAUACCAAGGUACCCCUUCUGGAAAUCAAAAAAGCGUGCUUCUCGGCAUACAAUUCCGGGCGAGCGGAGAGAGACGUCAAGGUAAUUAGCGCAUCCUGUGGAAAUCAAUCUCUUAUUUAUGUUAGCAGGUGCGCCAAAAAGUGUUACCGCGGCGUACCAAGUUGGCUUGCAGGACGGAUCUCUCUCUUAUAUUCCCUGCUUCCUGCGCUCGCUCCACUCGUGAAUGCCGUUCGUACAAGGAAGGGGAAAGACGGCGGGAACUAUUUACAUUGCCACACCUAUUCGGGCGGGUCUCUGACCCAAAAAAAUCGCCCACAGCCUGACUGUACGUCCACAGCGGCUAUCGCUGAAAAGCGACAAAACAUCGCCACUUUAGUCUAUGUUAUACUAGUUCGGUCGCCCCUAGCGAAGGAGUGUGAGAGUAGAACCGGCAAACGCGCUAUGCUGAGCUACAUAAAACUAGCAUCCAAGUUUUUACCCCGGAACCAUGGACGGCGUAGAACCCACCUGGCACCUACGCGACGUGUGGGGAUGGACGUCAGCAGAGGGAAAGGGAGAGGCACUACGCGGGUAGACCACCGGAAAGCCAACCCGUCCCAUUGCACUCUUCGGCCUAUGCCACUGGGGUUUAGAGCCAUAUGUUCUGCUCUCAGGUCGGUACACGCUUGUGAAGAUCUAAACCUUCUCGGUUACGAAGUGGUUACAAUGAGAAGAACGCUGGGCUGCCAGUUCCUGAACUACCUGCCAGGAAGCAGCAGAUGUUCUCUACUUUAUGGAUUGGCUAAUUUGAACGCUUACCUAACACGUCCCCGACCCGCCGUAAAUACAGCGCUCCUGGUUUGGCAGAGUGUCUACCCUUACUUGCACUUCGUCGUCGGGCCAUACGAGGUCCGCUCAUCUCACUUUCCGGAUUACUUGGUUAUCCCCAAGAUCCCAGUUCGUACUCUUGUGCGUCCAUCAUUUAAAGGGUGCUGGAUCGCGAUUCAGGUGGAUUUACUUUUACUGAACCCUUACCGCAGCGCUCACGUCGGCCGGGCCGUAAGUAGACAACGGCUGAAAUAUCAACACCUCAUCGUCCAGCCCCCGGGAACUUCAGGAACUGUGCGAAUCAGGCUAUAUGCGCCUUUUAAGUUGCUCAGGACUGACACUACGAUAUGUCGCUGUGGCCAGGUCGUAGCUAUUCCCUCGCAGAGGCCAACGGAACUUGAGCGGCUACCCAGUCGCGUAAUCGAUCGUGCACGUAGAGAACGACUAGGGGAAUGUAAGAUUCCCCUUGCCCGGACUUUUGCUAUUGAGUCGACUUUGAGCACUGUCGCAUUCCGUUUGGGUAGUUUAAAUAUCUGCGAAAGAGUAUAUAUAAAAUCUGAUAGGUUCUUCGGAACAGAUGUGGACGCCUGGGUGCAACGAGUUGGAGAUGGGCGUAGUUGGGAACCACGCCCGUUGGUCCAUACAGCCACCCUUAGAGUCGUCAUGUGCCCCGUACAUUUGUUUCCGGCAGUCCAUGGUACUCAAUUCACGCGGCGAGGUAAGGGUGUUUCGAAGGUCCCAAAGAAAACAUACAGACGUGAGGACGAAUCCCCUUGCUUAUUGAACUCCUACAAUCCCUGUGCGGCAACUGUGCCGGCCAGGACAGAAUUAUUUGGUAUGUGGAGUGCUGCCCGCCGCGGUCUGGACUCUCACCAUAGGACGGCUGAAUGUUCUAGAUUCAGCCGCAGGUUGGAAGUGACGGGAUUGACCGUAAUCUUAGACUCCAGGACACCGAUCCCACCAUUUUUUGCGCAGGCAGCGGUUCGUAGUCCACUUACUAGUGUGCUUCAAUUUGAGGCACUAUCAUCGUUUCGCAGGCAUGAUCCGGUGGGUAGGACGGCUAGGGCUAGAUGCUUCGGCGUUGCUGUGACGCCUAGUGGCCCGACGCGCACGGUUUGCAAAGCAGAACCAGUACCUUACCUUGUUACGGUCAGCGCAGCUUCGGUGAGAUCUCCCUGGUGCGGGCUGCCAAAGUCUGUGCGACCCUGCAUGCCUUGCAGGCAUCAAUCUAAAGGAUAUCGACAAUGGAAUUGGUAUCAUGAGGCAUUCAGUCCUGGAUACGCCCGGAUAUGUUUAGAGUGCAGCAUAUGUUCGCAUACAGAAUUCAAUACCGAGACUAUGCCUCUAUCGUCGGAUAGUCCUCCGGGCAACGAGGGACAUACCCCACACCUUUAUCAGCGUUCCCAACUUAGUUCAGGUAUGCAGGCUCAAAUGAGUCUCCGGGAAUCGCAGUGCGGCCUUACGGGCCGGGUAAGCAUACAUUUCGUAGAGCUGUUUUUCCAGGACUUGGCCCUCACCGGCCAGCAAGACCUACUUCAGUCCUUAGGGAAUCCGAAUCUUGUAAACACUCGCUGUGAUCCAGUGGGUAUGCGUGAUAUACACCUGAGGCGUCCCGCUAUUAAGCGCCGGUCGAGGUAUGUGGUCCAAGAUAGUGUACCUAAUAAAGAUAUGUCAUUGACGCUGACUCCCGCUAAAACAGCAGGCGUCCACCUCGGUAGCAUGAGCGUUGAGCCUACCCGAUGUUCAGCUUCUCCCACUCGGGUUAACUCGUUUAAGCACAGACACUGGUCUUGCCGACUUAUUCGUGGUCGCACGUCUGAUCGUCAACACUACCUUGCUUACUUCCGGGGACAGUAUUGCCUAGGGGAAGGCGUCGAGCGGCUUCACCUAGUCCCCACUCUUCUGCUAGUUCCAGCAUUUCUAACUGCGAAACCGAGGGCCCGUACAGGGAGCUCGAAAUCGGGAUCACCCGUAACUGAGGGGCUAGAUAAUAUUGGCUUUUAUGAUCUGUUGUCAGAUAACCGUACAAACUCCGACGGAGGUUCACGUCGCUGCCGGGUGAAUAAGAUUGAAUUUAUACACAUCCCAUAUGUCUCAAAAAAACAGCUAAAGAUUUUACAUCCCGGGGGUUGGACUCUUAACAUAGGCAAUGGGUUGCGUUUGCAGUUCCGAGGUUCUUCAUGUAUCCAUCCGGACUGGCUCGAACUGAUGUAUCCCUAUACGCGCAGGCAAAAGCGCCGCGAAAUUAUAACCCUGCGAGCUCGGUGCAAGUACAGUUUCCGACUUACUUAUGCUUGUAAGAAUCGGCGCGCUUCCUUCUAUGCUUUUCAGAGAUCUGUUUCAAUUACGACGCGGACUUUCCUUCCCGUCGAGAGCGAAGUUACUCAUCUAACUUUCGGCAAGAGCUCGAGGCGUGCCGGUAUGGGGCAUUUUAUACCACGAUUGCAUUCGACAUUUGUCCUGGAUGUAGCGUCCCACAGCGCUCAUACCAGUUCCUGUGUUUUUCAAUCCAGGAUGGAUGCUCCCUGUAACAGGGCAAACUCCGCUACUUACUUAUGUAAAUUGCCCGCCCCGCAUGUUGUGUUCUUGGGAAGGUAUCAAUGCACCCCACUCGAGUCAUUAACCGCAGUUUUUGUCUCGUCCCCAGAUCGCGAGGCUUUUUACGACCAGAACAUCGCAGUAUUUUCACGUGCUUUAGUGGAAAGUGAAGACACAGCACAGACCUCUACUUUUUCUCCCAGGGCGGCCCCCGACGCUAAAUUCUACUCAUGGAAAAUCCACGGUAUAUUUCGCUUUGAAAUGAGAGGAAAUCUCGAAUAUUUUAGCUGUAUCACACCACGACAGUCUACACAGUACACCGCCCUUAGAAAGGAAGAAGUUUUCUGGGUUUGCCCCUUACACGUCAUUCAGCCAAAUUCGAUAUUAAUUGAAGCAAUACCACUGAUGAAGGUUAGGGUGGUUACAUAUGAGGUAUUAGCAGUCCGUGUGUCCAGCCGAGAUUUGCCAGAGCCUAUCACUCAUUUAUAUUCUAGUAGGGCUCUCCCAGCGCUUUCUGGUGACCGGAGUAAAGAGAUCACAAGACCUUGGCUAUCCGAGCUCAGAGACGGAAUGUUACUGCGCGUGGGCGGCAUUUCGGGGUCCUACCAAGUUCAGCUUUCUUAUAGACACGGUGUUUCGGCCCUUAACGCUGCUAUCACAAAGCUUGCUGGGUCGCCCGAUGGGAAUCUGACACCGUUAUCGAUCGCGUUGAACCGCCCUCAGUUGCCUUGCCCAGCGUCGCUACGACUGAGGAUCAGCCGCGACCUGCCAGAUUGGCAGGCUGGCUCUUGGAAUCGCUUCGAAGAAAACAUACACUCCGGAUCCGUAGACUUAAGUCCAGGUGUCUCCAUCCAGUGCCCCCGCCCCCUAGUAUUCUACUCUAGUGCAAGCGUUCACGUAAGUAGUGGUGAACGCCGUGGUACAGGCGUAGGUUCUUUAAUAGAGGGUUGGCUCAGGAUACGCGGAAAACUCAAGAACACUUGGGAAGCUCCCAGAGACUAUUGGGUAGUUAAGCUAAUGUCAUGGCGGCACAUCUUGAUGGGGAAUUCAAUUCAACCCGGGUGGACAACCAGGCGGGUGGUCAAACUAGCCAUGAUGUUUUGUCUUAAGUCGGUUGACCGCUUUGGUAAGAGCUCUAUUUGCUACGGGAAAUACACGCACUUGAAUGACAGCAAUUUAAGAUUAGGUAUAGGCUCCACUACCCGUUGUUCAAUUCACCUAAUUCUACUACCGUGGCGGAGGCCCGCGCUGAUGGACACCCAGUUCCCAAAAGCUCGAUCCUCUCUUGGUGCGUGUACCCCUAGGGUACCAAAACCGGUAUUUUAUCCAUGUGCUAUGGCAGCUUCAUCUCAGCAUUGCAUUUGUGGACAUUAUGUAAGUUCUGAAAUAGCUACGUUAUCGCCGGGCCGCCUAACUGCCAAUAAUCUGAAGUCGCUACGUCCUUCGUGGAGCGACUCAAACACACCAAUUGGAUCAUUUUGGGUUUUACUUGGGCACCCACUGUCCCCUCAAGCCUCUCACUUCACAGUUGGCCCCCACCACGACGUAUUACUGCACUUAAUCCAGCUUCCCUGCUGGUCUAUAACGGAUGGUCCCAUUGUGGCCGGCCGGGAAACACGCUGGUAUACAGUGCAGACUGCUAUGCUGGCUCAGCGUACCUAUAUGAACUGGGGCUGCAGUCUAGUGACAUGCCAUGUGGCUACGACCGUGUGUAGUAUAACUCGCAGAACUUACUGUGCGACGCGAAAGCGAAGACGCAGAUCAGAAAGCCCAUCUCUCAUCUCAGUUCACCCUUCAUGGUGUAUUAGAUUUAUACCCCCGGGACGAUAUUGCUUCGCUUCGCGGUUGGGCGCAGACACAAGGGACCCCCAAACGGGGGCCGGUCCGGGAAAGGAGGUCCGCAACCACGUUGCUAGCGGGGUAGUUGACGACUUGAGAUUCUUAACGAUAAUCGGAGCGAGUGUCAAUGCGAUGCAAAGGGAUGGAGUGAUGUUAAGAGAUCCAAACGCCAAAUGGUCAAUCUGCUCCAACCCGGCUCCUAGCAAUGAUAGCUCCGGUGCGUUAUACGUUGGUCUUAAUCCGGCCCCGACGGCCGCUGUUUGCCAAUUUAAUUUCCCCACGCACCCGUCUUUCUCCCCCUGGCGUAGGUCACUAAAACUCCACACAAUCGCUAUUACAGUUCAGAGUCAGCGAUGCGCCCCGCGUCAGUACGCUCUAACAGUUGCUAGGGGGGCUUCGCAACCUGAAGAACGAAUACUCGGGAUGCGUUCUUUGGCUGCAGACCAAGAUUCUCCUUGCCACGGGAGGACUAGGUCGAGGGGAGGAUCAAAAUUUGUCUUGUGGGAAGGAGUAUUAUUCACCUGCGUCUGCGGACGGAGAAAGAACUUUUGCGAGAACAGUUGGCGUGACCCAGCACUGGCGCGAUGCCACGCCGCUGAUAGUCGCUAUCCCUCUACACAUUCGGGAUUCGGCAAUGCGGCAGCCUCAUUCAUUUGCGACUUGAAGAGAGCCGGGGUCCGACCGACGGGAGUCUUAGGAAUGGCCCACGCCUUAAUGAGGCAGAAAGGUCACGUCGCGAUUGAAUUAACAACGUACGCUAAGGACUUCCCGUUAAGCCGGUGCGGAAGCGGGGGCUCGAGUGUGAUCUUGUGUACUCACGGCCAGCGUAUUUAUGAUUCUGUUGUUGCGCAGGCUGAGAGAUUUUAUGUUGGCUGUUGGAAGCUAUGCAUAGACUUGGGGAGGCUCCUGCCUAGAGCGGGGAUAUUAAUUCUCAUUGCUUUUCUCAUAGUGCAGGUAGCUGCUGGUUACUUCUCUAGAGUACGAAAUGGCUCUAAUCUCGUGGUCAGUUACCACCCUGAAUGCUCGAUUCCACGGUUUGCGAGGGCGGAACGAAUGGUUGAGGGUAAGCUGGAAGGGCUUCGGGCCUUCUAUCAUCUCCCAGAGAGGUGGUAUUGGCAUCGGGAGAACACAGCGUUGUCGGCUACAGGUAUAACUUGCGAGAGACACCUACACUUCACAUUCCUUACAUCGACAUACCAGAAUUGGACUUUUGUCGCCCACAUCGCCGCACCGGUGCCGCUGUUAAACAUCAGACGUAAUGACCCGUCUCCCGAUUCCAGUGGGCUCAUUCUACGGGCAGACCGUUCGAUGUUGUGCCCAGUUCGGGCGUUUGGUGUACGCCCCGCUUGUGUGAAACGAGGCCCAUACGAUGUCAUCAAGUUGUUGCCCCUAGCAUCGGGCAAAUUAUUUCCUGCUCAGCCGUCACCCGUCUAUUCCUGUUCCAAAUUAGAGAAUCAGUUGAGCAUAGCUGAGAAGGGUCUCAUAGGUAGGGUGGCCGCGGCCUUAAAUGAUCACCGAAGGUUUCCUUCGUACGUGUGUCGACUUGGCUGGUUGCCUUGUCGCUCAACAAGGACGAACUUCAUAGUUUUAGUUAUAAAACAGCCGAGCCUUUUAAGGAGGCGGGGCAGACGCAGUGGGGACUGGUUGCACAGCCUUGGGGGACAGGGGAACACGAUUGAUAAGUCCGUCAGGUGUAACGUACGACGAAGUUACGGUGACUGCUGGAAGCCAACUUCAAUCAGGGGAGUGGAGUCGCCCGAGGGUUCCCUAGGACGAAGCAUCUGGUCAAGAAGACACGUUCUUCAGUCUCCCAAUACGAUCGCCGAUCUACAUUUCGAAUGCGAUAAGGUGCGUGGCAUAAGAGUCUUAACCGAGAUCGUGGAAAAGACCGCACAACAUAGGCCAGACGCGGCCUGGGAGAGCCACACAUUCCACCCAUGUGCACUUCACAUCAUCCGGAUUAGACUGCUCUAUCGGGUAAAACUCCCGCUAGAUGUCUCCUCGAACUUGGCGGGAGAUGAUAUUAGCACGACCUCCGAUGGAUUUAAACUCACAUGGCGGGUAAUGACACCAGGGAGGGUGCCGAUUCCGUACCUGUAUGGAUAUCAGAGUGCCUGUUCCCAGGCUAGCGCCUCGAAUUGA'
#print ProteinTranslation(rna)

integer_mass_dict = IntergerMassDictionary()
peptide = 'WGEGLYPWQVREIDFAYCLYTVLTWAETSIEWVDRESHHQLH'
l =  LinearSpectrum(peptide, integer_mass_dict)
l = ' '.join(map(str, l))
print l









