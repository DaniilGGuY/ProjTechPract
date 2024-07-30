#!/bin/bash

rm ./pictures/*

python3 ./make_postproc.py ./measure/reses/adress_mon_0.txt ./measure/reses/adress_mon_2.txt ./measure/reses/index_mon_0.txt ./measure/reses/index_mon_2.txt ./measure/reses/pointer_mon_0.txt ./measure/reses/pointer_mon_2.txt ./pictures/mon_array.png
python3 ./make_postproc.py ./measure/reses/adress_rand_0.txt ./measure/reses/adress_rand_2.txt ./measure/reses/index_rand_0.txt ./measure/reses/index_rand_2.txt ./measure/reses/pointer_rand_0.txt ./measure/reses/pointer_rand_2.txt ./pictures/rand_array.png
python3 ./make_postproc_errorbar.py ./measure/reses/adress_mon_2.txt ./measure/reses/index_mon_2.txt ./measure/reses/pointer_mon_2.txt ./measure/reses/adress_rand_2.txt ./measure/reses/index_rand_2.txt ./measure/reses/pointer_rand_2.txt ./pictures/errarbar.png
