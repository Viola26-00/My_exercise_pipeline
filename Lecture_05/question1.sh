!#/bin/bash
i=0
while read myfile
do
#if I do not use $(()) i+1 will be saved in i 
 i=$((i+1))
# because  myfile is a variable  the results will be words  therefore use <<<
 country=$(cut -f7 <<< "${myfile}")
 echo -e "${i}\t${country}"
done < example_people_data.tsv
