#!/bin/bash
current=`date "+%Y-%m-%d %H:%M:%S"`
timeStamp=`date -d "$current" +%s`
currentTimeStamp=$((timeStamp+`date "+%N"`/1000))
train_simple_WN18RR.py ./benchmarks/WN18RR/
./openke/data/data_process.py
train_simple_WN18RR.py ./benchmarks/WN18RR_1 currentTimeStamp