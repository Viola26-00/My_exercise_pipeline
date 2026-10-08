#!/bin/bash
#exclude header
i=0
tail -n +2 example_people_data.tsv |
while read myfile
do
#exclude blank so use test -n "${myfile}" to check if the string is greater than 0
~string needs double quotation marks
 if test -n "${myfile}"
 then
  i=$((i+1))
  country=$(cut -f1,3,7 <<< "${myfile}")
  echo -e "${i}\t${country}"
 fi
done 
#no need to write file here  because the pipeline already provide the file
