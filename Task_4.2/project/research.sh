#!/bin/bash

./clean

step="$1"
maxsize="$2"
exp="$3"

if [ "$#" -ne 3 ]; then
   echo "Error numver of args (3)"
   exit 1
fi

 if [ "$maxsize" -gt 500 ] || [ "$maxsize" -lt 0 ] || [ "$step" -lt 0 ] || [ "$exp" -gt 10000 ] || [ "$exp" -lt 0 ]; then
   echo "ERROR PARAMS (0 < exp < 10000) and (0 < maxsize < 500)"
   exit 2
fi

./build_apps.sh
./create_data.sh $step $maxsize $exp
./make_preproc.sh $step $maxsize $exp
./make_postproc.sh

