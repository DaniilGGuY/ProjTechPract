import math as m
import sys

step = int(sys.argv[1])
maxsize = int(sys.argv[2])
exp = int(sys.argv[3])

a = list()
for i in range(0, (maxsize // step + 1) * exp):
    a.append(float(input()))

for j in range(0, (maxsize // step + 1) * exp, exp):
    arr = a[j:j+exp+1]
    arr.sort()
    mx = arr[len(arr) - 1]
    mn = arr[0]
    avg = 0.00000000000001
    for i in arr:
        avg += i
    avg /= len(arr)
    s_sq = 0.0
    for i in arr:
        s_sq += (i - avg) * (i - avg)
    s_sq /= (len(arr) - 1)
    s = m.sqrt(s_sq)
    std_err = s / m.sqrt(len(arr))
    rse = std_err / avg * 100

    print(j // exp * step + 1, "{:.2f} {:.2f} {:.2f} {:.2f}".format(avg, rse, mx, mn))

