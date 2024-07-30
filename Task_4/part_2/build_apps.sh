#!/bin/bash

gcc -O0 -o ./apps/app1.exe ./progs/adress_mon.c
gcc -O2 -o ./apps/app2.exe ./progs/adress_mon.c
gcc -O0 -o ./apps/app3.exe ./progs/adress_rand.c
gcc -O2 -o ./apps/app4.exe ./progs/adress_rand.c
gcc -O0 -o ./apps/app5.exe ./progs/index_mon.c
gcc -O2 -o ./apps/app6.exe ./progs/index_mon.c
gcc -O0 -o ./apps/app7.exe ./progs/index_rand.c
gcc -O2 -o ./apps/app8.exe ./progs/index_rand.c
gcc -O0 -o ./apps/app9.exe ./progs/pointer_mon.c
gcc -O2 -o ./apps/app10.exe ./progs/pointer_mon.c
gcc -O0 -o ./apps/app11.exe ./progs/pointer_rand.c
gcc -O2 -o ./apps/app12.exe ./progs/pointer_rand.c

