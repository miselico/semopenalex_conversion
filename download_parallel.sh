#!/bin/bash

# source: https://web.archive.org/web/20240522151359/https://www.baeldung.com/linux/wget-parallel-downloading

mkdir data
cd data

cat ttlfilesSOA_no_star.txt | xargs -n 1 -P 10 wget -q 

cat ttlfilesSOA_only_star.txt | xargs -n 1 -P 10 wget -q 

