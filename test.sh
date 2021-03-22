#!/bin/bash
python train_simple_WN18RR.py ./benchmarks/WN18RR/
python ./openke/data/data_process.py
python ./benchmarks/WN18RR_1/n-n.py 141442 5000 5000
python train_simple_WN18RR.py ./benchmarks/WN18RR_1 1