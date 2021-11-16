import pandas as pd
import numpy as np
class REG_LINEAR():


    def __init__(self, sumbuX, sumbuY):
        self.sumbuX =  [float(i) for i in sumbuX.split()]
        self.sumbuY =  [float(i) for i in sumbuY.split()]
    
    def __tabel(self, NKsatu, NKdua, NKtiga, NKempat, NKlima, NKenam, Ksatu, Kdua, Ktiga, Kempat, Klima, Kenam ):
        
        data = {NKsatu: Ksatu,
                NKdua : Kdua,
                NKtiga: Ktiga,
                NKempat: Kempat,
                NKlima : Klima,
                NKenam : Kenam,
                }
                                                        
        table = pd.DataFrame(data,index=[i for i in range(1,len(self.sumbuX)+1)])
        print(table)

    def penyelesaianMetodeProscak(self):
        perkalian = []
        pangkat_X = []

        # hitung x kuadrat dan x kali y
        angka = 0
        for i in range (len(self.sumbuX)):
            pangkat_X.append(self.sumbuX[angka]**2)
            perkalian.append(self.sumbuX[angka]*self.sumbuY[angka])
            angka += 1

        # hitung b1 dan b0
        b1  = ( sum(perkalian) - sum(self.sumbuX)*sum(self.sumbuY)/ len(self.sumbuX) ) / ( sum(pangkat_X) - sum(self.sumbuX)**2 / len(self.sumbuX) )
        b0  = (sum(self.sumbuY) - (b1 * sum(self.sumbuX)))/ len(self.sumbuX)
        persamaanRegresi = f"y = {b0:.3f} + {b1:.3f}x"

        # HITUNG ESTIMASI KESALAHAN
        Y_hat = []
        RSS = []
        bil = 0
        for i in range(len(self.sumbuX)):
            Y_hat.append(b0 + b1*self.sumbuX[bil])
            
            RSS.append((self.sumbuY[bil] - Y_hat[bil])**2)
            bil+= 1 
        kesalahan = sum(RSS) / (len(self.sumbuX) - 2)

        korelasi = np.corrcoef( self.sumbuX, self.sumbuY )


        #tabel pertama
        print('------------------------------------------')
        self.__tabel('X  ', 'Y  ', 'XY   ', 'x**2  ', 'Yi', "(Yi - Y'i)**2", self.sumbuX, self.sumbuY, perkalian, pangkat_X, Y_hat, RSS)
        print(f"sum {int(sum(self.sumbuX))}  {int(sum(self.sumbuY))}    {int(sum(perkalian))}   {int(sum(pangkat_X))}        {int(sum(Y_hat))}         {sum(RSS):.2f}")
        print()
        print(
            f"b   = {b1:.3f}         ;     a  = {b0:.3f}\n\n"
            f"Persamaannya adalah {persamaanRegresi}\n"
            f"Korelasinya adalah {korelasi[0][1]:.5f}\n")

 

    def tampilkanData(self):
        print(self.sumbuX)

y = "18 24 36 48 36 36 36 35"
x =  "392 463 590 491 402 466 275 231"

permasalah_1 = REG_LINEAR(x, y)
permasalah_1.penyelesaianMetodeProscak()
