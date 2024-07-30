#!/bin/bash

step="$1"
maxsize="$2"
exp="$3"

rm ./measure/reses/*

cd ./measure/ || exit

for file in ./*.txt; do
  python3 ./../make_preproc.py "$step" "$maxsize" "$exp"  < "$file" > ./reses/"$file"
done

cd ./../ || exit

