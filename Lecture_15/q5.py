#!/usr/bin/python3
def kmer_counting(seq,kmersize,minfrequency):
	kmers=[]
	for i in range(0,len(seq)-kmersize+1):
		kmers.append(seq.upper()[i:i+kmersize])
	new=list(set(kmers))
	for k in new:
		if kmers.count(k) > minfrequency:
			print(k)
