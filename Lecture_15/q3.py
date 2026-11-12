#!/usr/bin/python3
def undetermined_base(seq, threshold=10):
	length=len(seq)
	count=0
	for base in seq:
		if base.upper() not in ["A","T","G","C"]:
			count=count+1
	undetermined_base_content=count/length*100
	if undetermined_base_content > threshold:
		return True
	else:
		return False

assert undetermined_base("nTCFGGACTt")==True
assert undetermined_base("ATGCTANCTN",20)==False

