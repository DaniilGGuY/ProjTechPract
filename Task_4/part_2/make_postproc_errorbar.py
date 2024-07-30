import matplotlib.pyplot as plt
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
f3 = sys.argv[3]
f4 = sys.argv[4]
f5 = sys.argv[5]
f6 = sys.argv[6]
save = sys.argv[7]

arr = list()
times = list()
sizes = list()
maxes = list()
mines = list()
f = open(f1, 'r')
for i in f:
    arr.append(i.split())
for i in range(len(arr)):
    times.append(float(arr[i][1]))
    sizes.append(float(arr[i][0]))
    maxes.append(float(arr[i][3]) - float(arr[i][1]))
    mines.append(float(arr[i][1]) - float(arr[i][4]))
f.close()

arr2 = list()
times2 = list()
sizes2 = list()
maxes2 = list()
mines2 = list()
f = open(f2, 'r')
for i in f:
    arr2.append(i.split())
for i in range(len(arr2)):
    times2.append(float(arr2[i][1]))
    sizes2.append(float(arr2[i][0]))
    maxes2.append(float(arr2[i][3]) - float(arr2[i][1]))
    mines2.append(float(arr2[i][1]) - float(arr2[i][4]))
f.close()

arr3 = list()
times3 = list()
sizes3 = list()
maxes3 = list()
mines3 = list()
f = open(f3, 'r')
for i in f:
    arr3.append(i.split())
for i in range(len(arr3)):
    times3.append(float(arr3[i][1]))
    sizes3.append(float(arr3[i][0]))
    maxes3.append(float(arr3[i][3]) - float(arr3[i][1]))
    mines3.append(float(arr3[i][1]) - float(arr3[i][4]))
f.close()

arr4 = list()
times4 = list()
sizes4 = list()
maxes4 = list()
mines4 = list()
f = open(f4, 'r')
for i in f:
    arr4.append(i.split())
for i in range(len(arr4)):
    times4.append(float(arr4[i][1]))
    sizes4.append(float(arr4[i][0]))
    maxes4.append(float(arr4[i][3]) - float(arr4[i][1]))
    mines4.append(float(arr4[i][1]) - float(arr4[i][4]))
f.close()

arr5 = list()
times5 = list()
sizes5 = list()
maxes5 = list()
mines5 = list()
f = open(f5, 'r')
for i in f:
    arr5.append(i.split())
for i in range(len(arr5)):
    times5.append(float(arr5[i][1]))
    sizes5.append(float(arr5[i][0]))
    maxes5.append(float(arr5[i][3]) - float(arr5[i][1]))
    mines5.append(float(arr5[i][1]) - float(arr5[i][4]))
f.close()

arr6 = list()
times6 = list()
sizes6 = list()
maxes6 = list()
mines6 = list()
f = open(f6, 'r')
for i in f:
    arr6.append(i.split())
for i in range(len(arr6)):
    times6.append(float(arr6[i][1]))
    sizes6.append(float(arr6[i][0]))
    maxes6.append(float(arr6[i][3]) - float(arr6[i][1]))
    mines6.append(float(arr6[i][1]) - float(arr6[i][4]))
f.close()

x_err = (int(arr[1][0]) - int(arr[0][0])) / 60

plt.xlabel("Размер матрицы")
plt.ylabel("Время, мс")
plt.grid()
plt.errorbar(sizes, times, yerr=(mines, maxes), capsize=x_err, label="Адресная арифметика (упорядоченный)")
plt.errorbar(sizes2, times2, yerr=(mines2, maxes2), capsize=x_err, label="Индексация (упорядоченный)")
plt.errorbar(sizes3, times3, yerr=(mines3, maxes3), capsize=x_err, label="Указатели (упорядоченный)")
plt.errorbar(sizes4, times4, yerr=(mines4, maxes4), capsize=x_err, label="Адресная арифметика (случайный)")
plt.errorbar(sizes5, times5, yerr=(mines5, maxes5), capsize=x_err, label="Индексация (случайный)")
plt.errorbar(sizes6, times6, yerr=(mines6, maxes6), capsize=x_err, label="Указатели (случайный)")
plt.legend()
plt.savefig(save)

