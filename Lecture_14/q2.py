#!/usr/bin/python3
#1
dna="ATGCATCATG"
k=2 # kmer size
n=2 # more than this number found

kmer=[]
for i in range(0,len(dna)-k+1):
	kmer.append(dna[i:i+k])
	

result=[]
for numbs in kmer:
	if kmer.count(numbs) >n:
		result.append(numbs)
print(set(result))
