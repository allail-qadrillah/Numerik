perhitungan = "24.53 56.94 97.24 78.48 24.53 56.24 92.24 27.47"
pengukuran  = "25 56 96 77 25 56 96 26"

def galat(hitung, ukur):
    # split spasi dari variabel menjadi list
    nilaiHitung = [float(i) for i in hitung.split()]
    nilaiUkur   = [float(i) for i in ukur.split()]
    # hitung setiap data menggunakan rumus Galat
    for i in range(len(nilaiHitung)):
        persentaseGalat = abs((nilaiHitung[i] - nilaiUkur[i]) / nilaiHitung[i]) * 100
        print(f"{i+1}. {persentaseGalat:.2f}%")

galat(perhitungan, pengukuran)
