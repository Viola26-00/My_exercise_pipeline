#!/bin/bash
#$ -cwd
#$ -N Arrayjob
#$ -t 1-20
#$ -o results_20/Myresult_$TASK_ID.o
#$ -e results_20/Myresult.e
#$ -V

./myanalysisprogram.sh ${splitdir2}/reads-${SGE_TASK_ID}
