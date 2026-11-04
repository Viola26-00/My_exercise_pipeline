#!/usr/bin/python3
import subprocess
subprocess.run("blastx -db ../Lecture_06/nem -query Coding.fasta -outfmt 7 > blastoutput_coding.out", shell=True)
print(open("blastoutput_coding.out").read())

subprocess.run("blastx -db ../Lecture_06/nem -query Noncoding.fasta -outfmt 7 > blastoutput_noncoding.out", shell=True)
print(open("blastoutput_noncoding.out").read())

