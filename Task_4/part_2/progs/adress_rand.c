#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>

#define N 10000

void gen_array(int arr[], size_t n)
{
    for (size_t i = 0; i < n; ++i)
        arr[i] = rand() % N;
}


void sort(int a[], size_t n)
{
    int pos = 0, tmp;
    for (size_t i = 0; i < n; ++i)
    {
        pos = i;
        for (size_t j = i + 1; j < n; ++j)
            if (*(a + pos) > *(a + j))
                pos = j;

        tmp = *(a + pos);
        *(a + pos) = *(a + i);
        *(a + i) = tmp;
    }
}


void copy(int dest[], int source[], size_t n)
{
    for (size_t i = 0; i < n; ++i)
        dest[i] = source[i];
}


int main(int argc, char **argv)
{
    size_t step = atoi(argv[1]), maxlen = atoi(argv[2]), exp = atoi(argv[3]);
    int arr[N + 1], arr_to_sort[N + 1];
    gen_array(arr, N + 1);
    
    for (size_t i = 1; i <= maxlen + 1; i += step)
    {
        for (size_t j = 0; j < exp; ++j)
        {
            clock_t beg, end;
            copy(arr_to_sort, arr, i);
            beg = clock();
            sort(arr_to_sort, i);
            end = clock();
            double res = (double)(end - beg) / CLOCKS_PER_SEC * 1000.0;
            printf("%lf\n", res);
        }
    }

    return 0;
}



