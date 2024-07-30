#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <sys/time.h>
#include <math.h>
#include <x86gprintrin.h>

unsigned long long microseconds_now(void)
{
    struct timeval val;

    if (gettimeofday(&val, NULL))
        return (unsigned long long) -1;

    return val.tv_sec * 1000000ULL + val.tv_usec;
}

unsigned long long calc_elapsed_time(const struct timespec *beg, const struct timespec *end)
{
    return ((unsigned long long)
        (end->tv_sec - beg->tv_sec) * 1000 * 1000 * 1000 +
                        (end->tv_nsec - beg->tv_nsec)) / 1000; 
}

int delay(uint32_t tms)
{
    time_t tv_sec = tms / 1000;
    long tv_nsec = (tms % 1000) * 1000000L;
    const struct timespec req = {.tv_sec = tv_sec, .tv_nsec = tv_nsec};
    
    return nanosleep(&req, NULL);
}

#define N_REPS 100
#define FREQUENCY 2600

void calc_res(long double res[], unsigned long long col_ms)
{
    double avg, s_sq, s, std_err, rse;
    
    avg = 0.0;
    for (size_t i = 0; i < N_REPS; i++)
        avg += res[i];
    avg /= 1000;
    avg /= N_REPS;
    s_sq = 0.0;
    for (size_t i = 0; i < N_REPS; i++)
        s_sq += (res[i] / 1000.0 - avg) * (res[i] / 1000.0 - avg);
    s_sq /= (N_REPS - 1);
    s = sqrt(s_sq);
    std_err = s / sqrt(N_REPS);
    rse = std_err / avg * 100;
    
    printf("AVG: %lf\nABS: %lf\nREL: %lf\nRSE: %lf\n", avg, fabs(avg - col_ms), fabs(avg - col_ms) / col_ms * 100, rse);
}

void calc_for_gettimeofday(unsigned long long col_ms)
{
    long double res[N_REPS];
    unsigned long long beg, end;
    
    for (size_t i = 0; i < N_REPS; ++i)
    {
        beg = microseconds_now();
        delay(col_ms);
        end = microseconds_now();
        res[i] = end - beg;
        printf("Number of dimension %zu: %Lf\n", i + 1, res[i]);
    }
    
    calc_res(res, col_ms);
}

void calc_for_clock_gettime(unsigned long long col_ms)
{
    long double res[N_REPS];
    struct timespec beg, end;
    
    for (size_t i = 0; i < N_REPS; ++i)
    {
        clock_gettime(CLOCK_MONOTONIC_RAW, &beg);
        delay(col_ms);
        clock_gettime(CLOCK_MONOTONIC_RAW, &end);
        res[i] = calc_elapsed_time(&beg, &end);
        printf("Number of dimension %zu: %Lf\n", i + 1, res[i]);
    }
    
    calc_res(res, col_ms);  
}


void calc_for_clock(unsigned long long col_ms)
{
    long double res[N_REPS];
    clock_t beg, end;
    
    for (size_t i = 0; i < N_REPS; ++i)
    {
        beg = clock();
        delay(col_ms);
        end = clock();
        res[i] = (double) (end - beg + col_ms * CLOCKS_PER_SEC / 1000.0) / CLOCKS_PER_SEC * 1000 * 1000;
        printf("Number of dimension %zu: %Lf\n", i + 1, res[i]);
    }
    
    calc_res(res, col_ms);  
}


void calc_for_rdtsc(unsigned long long col_ms)
{
    long double res[N_REPS];
    unsigned long long beg, end;
    
    for (size_t i = 0; i < N_REPS; ++i)
    {
        beg = __rdtsc();
        delay(col_ms);
        end = __rdtsc();
        res[i] = (end - beg) / FREQUENCY;
        printf("Number of dimension %zu: %Lf\n", i + 1, res[i]);
    }
    
    calc_res(res, col_ms);
}


int main(void)
{    
    
    calc_for_gettimeofday(1000);
    calc_for_gettimeofday(100);
    calc_for_gettimeofday(50);
    calc_for_gettimeofday(10);
    
    calc_for_clock_gettime(1000);
    calc_for_clock_gettime(100);
    calc_for_clock_gettime(50);
    calc_for_clock_gettime(10);
    
    calc_for_clock(1000);
    calc_for_clock(100);
    calc_for_clock(50);
    calc_for_clock(10);
    
    calc_for_rdtsc(1000);
    calc_for_rdtsc(100);
    calc_for_rdtsc(50);
    calc_for_rdtsc(10);
    
    return 0;
}
