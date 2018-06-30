#!/bin/bash

directory="/usr/local/spool/"
suffix="*.pcap"

fname_arr=(`find $directory -type f -name $suffix`)

for fname in "${fname_arr[@]}";
do
    cmd="bro -r "$fname" /usr/local/share/bro/site/local.bro";
    #echo $cmd
    eval "$cmd"
done
