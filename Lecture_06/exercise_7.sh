#!/bin/bash

#Task 1
awk 'BEGIN{FS="\t"}{if (substr($1,1,1)!="#") {print $2}}' blastoutput2.out
 
#Task2
awk 'BEGIN{FS="\t"}{if (substr($1,1,1)!="#") {print $4,$3}}' blastoutput2.out

#Task3
awk 'BEGIN{FS="\t"}{if (substr($1,1,1)!="#" && $5>20) {print $0}}' blastoutput2.out

#Task4
awk 'BEGIN{FS="\t"}{if (substr($1,1,1)!="#" && $5>20 && $4<100) {print $0}}' blastoutput2.out

#Task5
#when the next condition depends on the previous result or condition, we can use a nested if statement, which is written in the action block of the first if statement.

awk 'BEGIN{FS="\t"}{if (substr($1,1,1)!="#" && $5<20) {line=line+1
if(line<=20) {print $0}}}' blastoutput2.out

#Task6
awk 'BEGIN{FS="\t"} {if (substr($1,1,1)!="#" && $4<100) {print $0}}' blastoutput2.out | wc -l
#31

#Task7
sort -k12,12nr blastoutput2.out | awk 'BEGIN{FS="\t"} {if (NR<=10) {print $0}}'
#Use sort to sort the 12th field by numbers, and it will be listed in order from the largest to the smallest.

#Task8
awk 'BEGIN{FS="\t"} {if (substr($1,1,1)!="#" && $2 ~/AEI/) {print $7,$9}}' blastoutput2.out
#use tilde to check whether the second field contains the string "AEI", which is enclosed in slashes

#Task9
cut -f2 blastoutput2.out | sort | uniq -c | awk '{if ($0 !~ /#/ && $1>1){a=a+1}} END{print a}'
#23
#since the result of uniq -c is separated by space, we cannot use FS="\t".
#use uniq -c to count the number of non-redundant line

#Task10
awk 'BEGIN{FS="\t"} {if (substr($1,1,1)!="#") {result=$5/$4*100;print result "%"}}' blastoutput2.out

#Task11
echo -e "Group1:Bit score<100\nGroup2:100<=Bit score<200\nGroup3: 200<=Bit score<300\nGroup4: 300<=Bit score<400\nGroup5:Bit score>400"
#use echo to list all my grouping criteria

awk 'BEGIN{FS="\t"} {if (substr($1,1,1)!="#") {if ($12<=100){print $2,"Group1"}
else if ($12>100 && $12<=200){print $2,"Group2"}
else if ($12>200 && $12<=300){print $2,"Group3"}
else if ($12>300 && $12<=400){print $2,"Group4"}
else if ($12>400){print $2,"Group5"}
}}' blastoutput2.out

