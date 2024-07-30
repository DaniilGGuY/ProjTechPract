#!/bin/bash

step="$1"
maxsize="$2"
exp="$3"

./apps/app1.exe "$step" "$maxsize" "$exp" > ./measure/without_transp_0.txt
./apps/app2.exe "$step" "$maxsize" "$exp" > ./measure/without_transp_3.txt
./apps/app3.exe "$step" "$maxsize" "$exp" > ./measure/without_transp_s.txt
./apps/app4.exe "$step" "$maxsize" "$exp" > ./measure/transp_0.txt
./apps/app5.exe "$step" "$maxsize" "$exp" > ./measure/transp_3.txt
./apps/app6.exe "$step" "$maxsize" "$exp" > ./measure/transp_s.txt
./apps/app7.exe "$step" "$maxsize" "$exp" > ./measure/double_trans_0.txt
./apps/app8.exe "$step" "$maxsize" "$exp" > ./measure/double_trans_3.txt
./apps/app9.exe "$step" "$maxsize" "$exp" > ./measure/double_trans_s.txt

