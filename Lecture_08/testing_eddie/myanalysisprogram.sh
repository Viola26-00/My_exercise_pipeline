#!/bin/bash
guideRNAseq="ACATAAAACATCAAAGTGAACAGATTGTAGTGTAAGAAGTTAGATTAA"
while read line
do
 read line2 
 if [[ ${line2} == *${guideRNAseq}* ]]
 then
  echo -e "This sequence was found in ${line} ${line2}"
 fi
 done < $1

