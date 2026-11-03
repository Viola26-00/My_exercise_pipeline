seq="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
position=seq.find("GAATTC")
print(position+1)
print(len(seq)-len(seq[0:22]))

#The goal is to calculate the sizes of the two fragments produced when the sequence is cut by EcoRI. EcoRI recognises the motif GAATTC and cuts between the G and the A.

#Step 1: I store the sequence in a variable called seq, and use the find() method to find the position of the motif. It returns 21, which is the Python index of the G. Since Python starts counting from 0, I add 1, so the motif starts at position 22.

#Step 2: Since the cut is right after the G, the cut is between position 22 and 23.


#To get the length of the first fragment, I slice the sequence from 0 to 22, which takes positions 0 to 21, and then use the len() function to get its
#lenth, which is 22.
#For the second fragment, I use the len() function to get the length of the whole sequence, which is 55, and subtract the first fragment. That gives 33.
#22 plus 33 equals 55, so the two fragments add up to the whole sequence.
