#!/usr/bin/python3
def hydrophobic_aminoacid_percentage(seq,residue=["A","I","L","M","F","W","Y","V"]):
	length=len(seq)
	length_r=len(residue)
	total_content=0
	for i in range(0,length_r):
		residue_count=seq.upper().count(residue[i].upper())
		residue_content= residue_count/length*100
		total_content=total_content+residue_content
	return total_content

assert round(hydrophobic_aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(hydrophobic_aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(hydrophobic_aminoacid_percentage("MSRSLLLRFLLFLLLLPPLP")) == 65
