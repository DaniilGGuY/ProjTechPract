#!/bin/bash

step="$1"
maxsize="$2"
exp="$3"

rm ./measure/*.txt
./apps/app1.exe "$step" "$maxsize" "$exp" > ./measure/adress_mon_0.txt
./apps/app2.exe "$step" "$maxsize" "$exp" > ./measure/adress_mon_2.txt
./apps/app3.exe "$step" "$maxsize" "$exp" > ./measure/adress_rand_0.txt
./apps/app4.exe "$step" "$maxsize" "$exp" > ./measure/adress_rand_2.txt
./apps/app5.exe "$step" "$maxsize" "$exp" > ./measure/index_mon_0.txt
./apps/app6.exe "$step" "$maxsize" "$exp" > ./measure/index_mon_2.txt
./apps/app7.exe "$step" "$maxsize" "$exp" > ./measure/index_rand_0.txt
./apps/app8.exe "$step" "$maxsize" "$exp" > ./measure/index_rand_2.txt
./apps/app9.exe "$step" "$maxsize" "$exp" > ./measure/pointer_mon_0.txt
./apps/app10.exe "$step" "$maxsize" "$exp" > ./measure/pointer_mon_2.txt
./apps/app11.exe "$step" "$maxsize" "$exp" > ./measure/pointer_rand_0.txt
./apps/app12.exe "$step" "$maxsize" "$exp" > ./measure/pointer_rand_2.txt

