#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 500

typedef int matrix_t[N + 1][N + 1];

void init_matrix(matrix_t a, size_t n)
{   
    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < n; j++)
            a[i][j] = rand() % 1000;
}

void mult(matrix_t a, matrix_t b, matrix_t c, size_t n)
{
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            int element = 0;
            for (size_t k = 0; k < n; k++)
            {
                element += a[i][k] * b[k][j];
            }
            c[i][j] = element;
        }
    }
}

void copy(matrix_t a, matrix_t b, size_t n)
{
    for (size_t i = 0; i < n; ++i)
       for (size_t j = 0; j < n; ++j)
           a[i][j] = b[i][j];
}

int main(int argc, char **argv)
{
    size_t step = atoi(argv[1]), maxlen = atoi(argv[2]), exp = atoi(argv[3]);
    matrix_t source;
    matrix_t a;
    matrix_t b;
    matrix_t c;
    init_matrix(source, N + 1);

    for (size_t i = 1; i <= maxlen + 1; i += step)
    {
        for (size_t j = 0; j < exp; ++j)
        {
            clock_t beg, end;
            copy(a, source, i);
            copy(b, source, i);
            beg = clock();
            mult(a, b, c, i);
            end = clock();
            a[0][0] = b[0][0];
            b[0][0] = c[0][0];
            c[0][0] = a[0][0];
            double res = (double)(end - beg) / CLOCKS_PER_SEC * 1000.0;
            printf("%lf\n", res);
        }
    }

    return 0;
}

