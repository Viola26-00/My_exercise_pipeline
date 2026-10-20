#!/bin/bash
#$ -cwd
#$ -N Arrayjob
#$ -t 1-100
#$ -o results_100/Myresult_$TASK_ID.o
#$ -e results_100/Myresult.e
#$ -V

./myanalysisprogram.sh ${splitdir}/reads-${SGE_TASK_ID}
