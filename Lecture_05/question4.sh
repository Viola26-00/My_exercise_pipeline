#!/bin/bash
i=0
line=0
#name line variable  to exclude the header
echo -e "list:"
echo -e "name\tbirthday_month\tcountry"
#write it after while IFS only affect the read
while IFS=$'\t' read  name email city birthday_day  birthday_month birthday_year country
do
 line=$((line+1))
 if test ${line} -gt 1 && test -n "${name}" && test ${birthday_month} -eq 10
 then
  i=$((i+1))
  echo -e "${name} ${birthday_month} ${country}"
 fi
done < example_people_data.tsv
echo -e "Total number: ${i}"



#command | while...
#--while常在subshell
#--裡面改的variable外面拿不到
#--echo寫在外面跑的是原始的i=0 
#while... done < file
#--while 在目前的shell
#--裡面改的variable done後還能用

