try:
    print(x)
except:
    print("Ada terjadi kesalahan.")
else:
    print("Nilai x adalah", x)

print()

try:
    x = int(input("Masukkan angka: "))
    if not type(x) is int:
        raise ValueError

except ValueError:
    print("Bukan angka.")

else:
    print('Angkanya jika dikali 2 adalah', x * 2)

print()

try:
    print(a)
except NameError as x:
    print("Terjadi kesalahan karena", x)
except ValueError as x2:
    print("Terjadi kesalahan karena", x2)
except:
    print("Terjadi kesalahan.")
else:
    print("Berjalan dengan baik.")
finally:
    print("Program telah berjalan.")

print()

a = 2
b = 3
try:
    print("Apakah a lebih besar dari b?")
    if a < b:
        raise Exception
    else:
        print("Benar, a lebih besar dari b.")

except:
    print("Tidak, a tidak lebih besar dari b atau ada yang salah.")