import matplotlib.pyplot as plt
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
f3 = sys.argv[3]
f4 = sys.argv[4]
arr = list()
times = list()
sizes = list()
f = open(f1, 'r')
for i in f:
    arr.append(i.split())
for i in range(len(arr)):
    times.append(float(arr[i][1]))
    sizes.append(float(arr[i][0]))
f.close()

arr2 = list()
times2 = list()
sizes2 = list()
f = open(f2, 'r')
for i in f:
    arr2.append(i.split())
for i in range(len(arr2)):
    times2.append(float(arr2[i][1]))
    sizes2.append(float(arr2[i][0]))
f.close()

arr3 = list()
times3 = list()
sizes3 = list()
f = open(f3, 'r')
for i in f:
    arr3.append(i.split())
for i in range(len(arr3)):
    times3.append(float(arr3[i][1]))
    sizes3.append(float(arr3[i][0]))
f.close()

plt.xlabel("Размер матрицы")
plt.ylabel("Время, мс")
plt.grid()
plt.plot(sizes, times, label="Без транспонирования")
plt.plot(sizes2, times2, label="С транспонированием одной")
plt.plot(sizes3, times3, label="С транспонированием обеих")
plt.legend()
plt.savefig(f4)

