#!/bin/bash
#SBATCH --job-name=conver_trig_nt
#SBATCH --time=72:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=fatq

cd data

conda activate semopenalex
conda install rdflib==7.0.0

process_one(){
    python ../convert_to_ntriples.py $1 | lz4 -c -9 -z >  ${1%.trig.gz}.nt.lz4
    echo done $1
}
export -f process_one


ls -1 *.trig.gz | xargs -P 60 -I {} bash -c 'process_one "$@"' _ {}

