#!/bin/bash
#avoid script accumulating
rm question5_output/*.txt
i=0
line=0
while IFS=$'\t' read name email city birthday_day birthday_month birthday_year country
do
 line=$((line+1))
 if test ${line} -gt 1 && test -n "${name}" && test ${birthday_month} -eq 10
 then
  i=$((i+1))
  echo -e "${name} ${birthday_month} ${country}" >> "question5_output/${country}.txt"
 fi
done < example_people_data.tsv
echo -e "Total number: ${i}"
