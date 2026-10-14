#!/bin/bash
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
