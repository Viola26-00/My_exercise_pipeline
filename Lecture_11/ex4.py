seq="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1=seq[0:63]
exon2=seq[90:]
print(exon1)
print(exon2)

coding_seq=exon1+exon2
print(coding_seq)

print(len(coding_seq))

print(len(coding_seq)/len(seq)*100)

intron=seq[63:90].lower()
print(intron)

final_seq=exon1+intron+exon2
print(final_seq)


#The goal is to extract the two exons and join them to make the coding sequence.
#First, I store the sequence in a variable called seq.
#The first exon runs from the 1st to the 63rd base. Since Python starts counting from 0 and slicing doesn’t include the end position, I slice from 0 to 63 and store it in exon1.
#The second exon starts at the 91st base, which is index 90 in Python, so I slice from 90 to the end and store it in exon2. Then I print them out.
#To make the coding sequence, I concatenate the two exons using + and store the result in coding_seq.

#The goal is to calculate the percentage of coding sequence in the whole sequence.
#First, I use the len() function to get the length of the coding sequence, which is 96.
#Then I divide it by the length of the whole sequence, which is 123, and multiply by 100.
#The result is about 78.05%.

#The goal is to print the sequence with the coding bases in uppercase and the non-coding bases in lowercase.
#I already have the two exons, which are in uppercase, so I only need to get the intron and convert it to lowercase.
#The intron runs from the 64th to the 90th base, so I slice the sequence from 63 to 90. Then I use the lower() method to convert it to lowercase, and store it in a variable called intron.
#Finally, I concatenate exon1, intron and exon2 in that order using the plus operator, store the result in final_seq, and print it.
