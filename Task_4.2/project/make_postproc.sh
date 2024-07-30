#!/bin/bash

python3 ./make_postproc.py ./measure/reses/without_transp_0.txt ./measure/reses/transp_0.txt ./measure/reses/double_trans_0.txt ./pictures/opt_0.png
python3 ./make_postproc.py ./measure/reses/without_transp_3.txt ./measure/reses/transp_3.txt ./measure/reses/double_trans_3.txt ./pictures/opt_3.png
python3 ./make_postproc.py ./measure/reses/without_transp_s.txt ./measure/reses/transp_s.txt ./measure/reses/double_trans_s.txt ./pictures/opt_s.png
