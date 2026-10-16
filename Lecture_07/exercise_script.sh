#!/bin/bash
db=$1        # database, e.g. protein
query=$2     # search term, e.g. "Primates[Organism] AND HOXA7[Gene Name] NOT partial"
name=$3      # output file name without extension, e.g. hoxa7
win=$4       # window size, e.g. 4

# step 1: number of records found by esearch
c1=$(esearch -db "${db}" -query "${query}" | xtract -pattern ENTREZ_DIRECT -element Count)

# step 2: download the sequences in FASTA format
esearch -db "${db}" -query "${query}" | efetch -format fasta > "${name}.fa"

# step 3: number of sequences actually downloaded
c2=$(grep -c ">" "${name}.fa")

# stop if the download is incomplete
if [ "${c1}" -ne "${c2}" ]; then
    echo "Error: esearch found ${c1} records but ${c2} sequences were downloaded"
    exit 1
fi

# step 4: shortest and longest sequence length
min=$(infoseq -sequence "${name}.fa" -only -length -noheading | sort -n | head -1)
max=$(infoseq -sequence "${name}.fa" -only -length -noheading | sort -n | tail -1)

#step 5: stop if the sequence lengths are abnormal
if (( ${max} > 5*${min} ))
then
 echo -e "Error: sequence lengths are abnormal (shortest: ${min}, longest:${max})"
 echo -e "Please add the  length range to the query, e.g. '...AND 100:400[SLEN]' and run again"
 exit 1
elif (( ${max} > 2*${min} ))
then
 echo -e "Warning: sequence lengths vary considerably (shortest:${min}, longest:${max})"
 echo -e "Continuing, but please check the alignment and the plot"
fi

#step 6: alignment
clustalo --force -i "${name}.fa" -o "${name}.aln.fa"

c3=$(grep -c ">" "${name}.aln.fa")

#stop if the number of sequences changes after alignment
if [[ ${c3} -ne ${c2} ]]
then
 echo -e "Error: Number of sequences changed after alignment, please check the clustalo output"
 exit 1
fi

#stop if not all sequences have the same length
nlen=$(infoseq -sequence "${name}.aln.fa" -only -length -noheading | sort -n | uniq | wc -l)
if [[ ${nlen} -ne 1 ]]
then
 echo -e "Error: not all sequences have the same length"
 exit 1
fi

#step 7: plot sequence conservation
plotcon -sequences "${name}.aln.fa" -winsize ${win} -graph png -goutfile "${name}_win${win}"
