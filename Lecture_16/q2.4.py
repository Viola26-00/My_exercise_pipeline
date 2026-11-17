#!/usr/bin/python3
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translation(seq):
	codons=[]
	result=[]
	for i in range(0,len(seq)-2,3):
		codons.append(seq[i:i+3])

	for codon in codons:
		result.append(gencode.get(codon,"X"))
	
	return result

def reverse_complement(dna):
	dna2=dna.replace("A","t")
	dna3=dna2.replace("T","a")
	dna4=dna3.replace("C","g")
	dna5=dna4.replace("G","c")
	dna6=dna5.upper()
#if we don't store list(dna6) as an variable and use reverse(), it will return none since reverse() will modify the list directly and return none
	new=list(dna6)
	new.reverse()
	return "".join(new)

dna="ATGTTCGGT"
dna_final=reverse_complement(dna)

for j in range(0,3):
	print("Frame", j+1,":")
	print(translation(dna_final[j:]))
