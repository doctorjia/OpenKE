#!/bin/bash
current=`date "+%Y-%m-%d %H:%M:%S"`
timeStamp=`date -d "$current" +%s`
currentTimeStamp=$((timeStamp+`date "+%N"`/1000))
python train_simple_WN18RR.py ./benchmarks/WN18RR/
python ./openke/data/data_process.py
python ./benchmarks/WN18RR_1/n-n.py
python train_simple_WN18RR.py ./benchmarks/WN18RR_1 currentTimeStamp