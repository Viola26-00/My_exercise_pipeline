#!/usr/bin/python3
#use wc to see how many lines are in the plain_genomic_seq.txt, and it shows 1 line.
#use print(open("plain_genomic_seq.txt").read()) to see whether there is a \n at the end of the file.
#If there is one, it will leave a blank line after the sequence.
local_seq=open("plain_genomic_seq.txt").read().rstrip()

#check whether we exclude the \n successfully.
len(local_seq)

#remove non-ATGC nucleotides
#check which are not ATGC by using replace()
print(repr(local_seq.replace("A","").replace("T","").replace("G","").replace("C","")))

local_seq2=local_seq.replace("X","").replace("L","").replace("S","").replace("K","")

#convert the sequence to uppercase
local_seq3=local_seq2.upper()
 
exon1=local_seq3[0:63]
exon2=local_seq3[90:]
intron1=local_seq3[63:90]

#write each of these sub-seqs to individual files
exon1_file=open("Localseq_exon1.fasta","w")
exon1_file.write(">Localseq_exon1_length" + str(len(exon1)) + "\n")
exon1_file.write(exon1 + "\n")
exon1_file.close()
print(open("Localseq_exon1.fasta").read())


exon2_file=open("Localseq_exon2.fasta","w")
exon2_file.write(">Localseq_exon2_length" + str(len(exon2)) + "\n")
exon2_file.write(exon2 + "\n")
exon2_file.close()
print(open("Localseq_exon2.fasta").read())

intron1_file=open("Localseq_intron1.fasta","w")
intron1_file.write(">Localseq_intron1_length" + str(len(intron1)) + "\n")
intron1_file.write(intron1 + "\n")
intron1_file.close()
print(open("Localseq_intron1.fasta").read())


#AJ223353 goes through the same process as the previous one
remote_seq=open("AJ223353_noheader.txt").read().rstrip()
print(repr(remote_seq.replace("A","").replace("T","").replace("G","").replace("C","")))
remote_seq2=remote_seq.replace("\n","")
remote_seq3=remote_seq2.upper()

noncoding1=remote_seq3[0:28]
coding=remote_seq3[28:409]
noncoding2=remote_seq3[409:]


noncoding1_file=open("Remoteseq_noncoding1.fasta","w")
noncoding1_file.write(">Remoteseq_noncoding1_length" + str(len(noncoding1)) + "\n")
noncoding1_file.write(noncoding1 + "\n")
noncoding1_file.close()
print(open("Remoteseq_noncoding1.fasta").read())

coding_file=open("Remoteseq_coding.fasta","w")
coding_file.write(">Remoteseq_coding_length" + str(len(coding)) + "\n")
coding_file.write(coding + "\n")
coding_file.close()
print(open("Remoteseq_coding.fasta").read())

noncoding2_file=open("Remoteseq_noncoding2.fasta","w")
noncoding2_file.write(">Remoteseq_noncoding2_length" + str(len(noncoding2)) + "\n")
noncoding2_file.write(noncoding2 + "\n")
noncoding2_file.close()
print(open("Remoteseq_noncoding2.fasta").read())

All_coding_file=open("Coding.fasta","w")
All_coding_file.write(">Localseq_exon1_length" + str(len(exon1)) + "\n")
All_coding_file.write(exon1 + "\n")
All_coding_file.write(">Localseq_exon2_length" + str(len(exon2)) + "\n")
All_coding_file.write(exon2 + "\n")
All_coding_file.write(">Remoteseq_coding_length" + str(len(coding)) + "\n")
All_coding_file.write(coding + "\n")
All_coding_file.close()
print(open("Coding.fasta").read())


All_noncoding_file=open("Noncoding.fasta","w")
All_noncoding_file.write(">Localseq_intron1_length" + str(len(intron1)) + "\n")
All_noncoding_file.write(intron1 + "\n")
All_noncoding_file.write(">Remoteseq_noncoding1_length" + str(len(noncoding1)) + "\n")
All_noncoding_file.write(noncoding1 +"\n")
All_noncoding_file.write(">Remoteseq_noncoding2_length" + str(len(noncoding2)) + "\n")
All_noncoding_file.write(noncoding2 + "\n")
All_noncoding_file.close()
print(open("Noncoding.fasta").read())
