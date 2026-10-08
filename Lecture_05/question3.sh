#!/bin/bash
tail -n +2 example_people_data.tsv |
while read myfile
do
 if test -n "${myfile}"
 then
 country=$(cut -f7 <<< "${myfile}")
#because the filename has variable so add double quotation marks
 echo -e "${myfile}" >> "question3_output/${country}.txt"
 fi
done 
