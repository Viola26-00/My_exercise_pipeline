#!/usr/bin/python3

def amino_acid_percentage(seq,residue):
	length=len(seq)
	residue_count=seq.upper().count(residue.upper())
	residue_content=residue_count/length*100
	return residue_content

assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
