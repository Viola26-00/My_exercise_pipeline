seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a=seq.count("A")     #16
print(a)
t=seq.count("T")     #21
print(t)
result=(a+t)/len(seq)      #0.6851851851851852
print(result)

#The goal is to calculate the A+T content of the DNA sequence.
#First, I store the DNA sequence in a variable called seq.
#Then I use the count() method to count how many A’s there are, and store it in a variable a. That gives 16.
#I do the same for T and store it in t. That gives 21.
#Then I add a and t together and divide by the length of the sequence, which I get using len(). I put a + t in brackets so the addition happens before the division.
#The result is about 0.685, so the A+T content is about 68.5%.
