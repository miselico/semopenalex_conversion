#!/bin/bash
#SBATCH --job-name=conver_trig_nt
#SBATCH --time=72:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=fatq

cd data

conda activate semopenalex
pip install rdflib==7.0.0

process_one(){
    # this makes sure that if the first part of the pipe fails, $? is set to the return of the last failing part, and not the last one
    set -o pipefail

    if python ../convert_to_ntriples.py $1 | lz4 -c -9 -z >  ${1%.trig.gz}.nt.lz4 
    then
        echo done $1
    else
        echo failed $1
    fi
    
    
}
export -f process_one


ls -1 -S *.trig.gz | xargs -P 50 -I {} bash -c 'process_one "$@"' _ {}

