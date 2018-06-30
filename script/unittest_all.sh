#!/bin/bash
export PYTHONPATH=/root/helios/helios/app/

directory="/root/helios/helios/app/test/"
suffix="'*_test.py'"

declare -a fname_arr=(`eval find $directory -type f -name $suffix`)

for fname in "${fname_arr[@]}";
do
    echo $fname
    eval "coverage run "$fname
done

