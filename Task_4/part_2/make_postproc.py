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

arr4 = list()
times4 = list()
sizes4 = list()
f = open(f4, 'r')
for i in f:
    arr4.append(i.split())
for i in range(len(arr4)):
    times4.append(float(arr4[i][1]))
    sizes4.append(float(arr4[i][0]))
f.close()

arr5 = list()
times5 = list()
sizes5 = list()
f = open(f5, 'r')
for i in f:
    arr5.append(i.split())
for i in range(len(arr5)):
    times5.append(float(arr5[i][1]))
    sizes5.append(float(arr5[i][0]))
f.close()

arr6 = list()
times6 = list()
sizes6 = list()
f = open(f6, 'r')
for i in f:
    arr6.append(i.split())
for i in range(len(arr6)):
    times6.append(float(arr6[i][1]))
    sizes6.append(float(arr6[i][0]))
f.close()

plt.xlabel("Размер матрицы")
plt.ylabel("Время, мс")
plt.grid()
plt.plot(sizes, times, label="Адресная арифметика О0")
plt.plot(sizes3, times3, label="Индексация О0")
plt.plot(sizes5, times5, label="Указатели О0")
plt.plot(sizes2, times2, label="Адресная арифметика О2")
plt.plot(sizes4, times4, label="Индексация О2")
plt.plot(sizes6, times6, label="Указатели О2")
plt.legend()
plt.savefig(save)



