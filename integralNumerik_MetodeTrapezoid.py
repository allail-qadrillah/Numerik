import numpy as np

# soal yang akan dihitung
def func(x):
    return x**2 # tuliskan soal yang akan dihitung disini

a = 0    # batas bawah
b = 2    # batas atas
n = 6    # banyak pias (Trapesium yang digunakan)

n = n + 1

Dx = (b - a)/ ( n - 1) # delta x

x = np.linspace(a, b, n) # membuat urutan numerik dengan membagi sebanyak n

# menjumlahkan tiap tiap persamaan 
sum = 0.0
for i in range(1, n-1):
    sum += func(x[i])

hasil = Dx/2 * (func(x[0]) + 2*sum + func(x[n-1])) # rummus akhir

# tampilan penyelesaian
print(f"I = 1/2*{Dx}[ {func(x[0])} + 2({sum}) + {func(x[-1])}]")
print(f"I = {hasil}")


