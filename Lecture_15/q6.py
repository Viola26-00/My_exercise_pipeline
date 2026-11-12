#!/usr/bin/python3
def kmer_counting(seq,kmersize,minfrequency):
	kmers=[]
	for i in range(0,len(seq)-kmersize+1):
		kmers.append(seq.upper()[i:i+kmersize])
	new=list(set(kmers))
	for k in new:
		if kmers.count(k) > minfrequency:
			print(k)
while True:
	try:
		seq=input("Enter the sequence of interest: ")
#because the input of input() is string, we use int()
		kmersize=int(input("Enter the kmer length for analysis: "))
		minfrequency=int(input("Enter the threshold frequency of kmers found: "))
	except ValueError:
		print("Please enter an integer for kmersize and minfrequency")
	else:
		kmer_counting(seq,kmersize,minfrequency)
		break
