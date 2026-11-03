seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
seq1=seq.replace("A","t")
seq2=seq1.replace("T","a")
seq3=seq2.replace("G","c")
seq4=seq3.replace("C","g")
seq_final=seq4.upper()
print(seq_final)

#The goal is to get the complement of the DNA sequence.
#First, I store the DNA sequence in a variable called seq.
#Then I use the replace() method to replace uppercase A with lowercase t, and save the result in seq1.
#I use lowercase because if I replaced A with uppercase T, the next step, replacing T with A, would also change those new T’s back to A. Using lowercase keeps the replaced letters separate from the original ones.
#Then I take seq1 and replace uppercase T with lowercase a, and do the same for G and C, each step using the result of the previous one.
#At the end, the whole complement is in lowercase, so I use the upper() method to convert it back to uppercase, and print it.
