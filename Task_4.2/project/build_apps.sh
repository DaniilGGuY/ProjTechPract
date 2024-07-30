#!/bin/bash

gcc -O0 -o ./apps/app1.exe ./progs/without_transp.c
gcc -O3 -o ./apps/app2.exe ./progs/without_transp.c
gcc -Os -o ./apps/app3.exe ./progs/without_transp.c
gcc -O0 -o ./apps/app4.exe ./progs/transp.c
gcc -O3 -o ./apps/app5.exe ./progs/transp.c
gcc -Os -o ./apps/app6.exe ./progs/transp.c
gcc -O0 -o ./apps/app7.exe ./progs/double_trans.c
gcc -O3 -o ./apps/app8.exe ./progs/double_trans.c
gcc -Os -o ./apps/app9.exe ./progs/double_trans.c
