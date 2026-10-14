!/bin/bash

#Task1
while read  accession
do
 if [[ ${accession} != \#* ]]
 then 
  echo -e "${accession}" | cut -f2
 fi
done < blastoutput2.out


#Task2
while read al_pi
do
 if [[ ${al_pi} != \#* ]]
 then
  echo -e "${al_pi}" | cut -f4,3
 fi
done < blastoutput2.out

#another method
while IFS=$'\t' read -a result
do
 if [[ ${result} != \#* ]]
 then
  echo -e "${result[3]} ${result[2]}"
 fi
done < blastoutput2.out

#Task3
while IFS=$'\t' read -a result
do
 if [[ ${result} != \#* && ${result[4]} -gt 20 ]]
 then
  echo -e "${result[@]}"
 fi
done < blastoutput2.out

#another method
while read  result
do
 f5=$(echo "${result}" | cut -f5)
 if [[ ${result} != \#* && ${f5} -gt 20 ]]
 then
  echo -e "${result}"
 fi
done < blastoutput2.out


#Task4
while IFS=$'\t' read -a result
 do
 if [[ ${result} != \#* && ${result[3]} -lt 100 && ${result[4]} -gt 20 ]]
 then
  echo -e "${result[@]}"
 fi
done < blastoutput2.out

#Task5
i=0
while IFS=$'\t' read -a result
 do
 if [[ ${result} != \#* && ${result[4]} -lt 20 ]]
 then
 i=$((i+1))
  if [[ ${i} -le 20 ]]
  then
   echo -e "${result[@]}"
  fi
 fi
done < blastoutput2.out

#Task6
i=0
while IFS=$'\t' read -a result
 do
 if [[ ${result} != \#* && ${result[3]} -lt 100 ]]
 then
 i=$((i+1))
 fi
done < blastoutput2.out
echo -e "${i}"
# echo should be put after the while loop so the total count is printed once

#Task7
i=0
sort -t $'\t' -k 12,12nr blastoutput2.out | \
while IFS=$'\t' read -a result
 do
 if [[ ${result} != \#* ]]
 then
 i=$((i+1))
  if [[ ${i} -le 10 ]]
  then
   echo -e "${result[@]}"
  fi
 fi
done

#Task8
while IFS=$'\t' read -a result
 do
 if [[ ${result} != \#* && ${result[1]} == *AEI* ]]
 then
   echo -e "${result[6]} ${result[8]}"
 fi
done < blastoutput2.out

#Task9
#because the result of uniq -c is separated by space, we have to set IFS=" "

cut -f2 blastoutput2.out | sort | uniq -c | \
while IFS=" " read -a result
 do
#since the first field of result is count, the condition has to change to that the whole line doesn't include #
 if [[ ${result[@]} != *\#* && ${result[0]} -gt 1 ]]
 then
  echo -e "${result[@]}"
 fi
done |\
wc -l

#Task10
while IFS=$'\t' read -a result
do
 if [[ ${result[@]} != \#* ]]
 then
 outcome=$(echo "${result[4]}/${result[3]}*100" | bc -l)
#$(())can only be used to calculate integers, so we have to use bc -l
  printf "%.2f %%\n" "${outcome}"
#printf can round the result to 2 decimal places;%% prints a literal % sign
#we have to add \n after the result since printf won't automatically add a new line
 fi
done < blastoutput2.out

#Task11
echo -e "Group1:Bit score<100\nGroup2:100<=Bit score<200\nGroup3: 200<=Bit score<300\nGroup4: 300<=Bit score<400\nGroup5:Bit score>=400"
while IFS=$'\t' read -a result
do
 if [[ ${result[@]} != \#* ]]
 then
  if [[ $(echo "${result[11]}<100" | bc -l) -eq 1 ]]; then echo "Group1 ${result[@]}"
  elif [[ $(echo "${result[11]}<200" | bc -l) -eq 1 ]]; then echo "Group2 ${result[@]}"
  elif [[ $(echo "${result[11]}<300" | bc -l) -eq 1 ]]; then echo "Group3 ${result[@]}"
  elif [[ $(echo "${result[11]}<400" | bc -l) -eq 1 ]]; then echo "Group4 ${result[@]}"
  elif [[ $(echo "${result[11]}>=400" | bc -l) -eq 1 ]]; then echo "Group5 ${result[@]}"
 fi
fi
done < blastoutput2.out
