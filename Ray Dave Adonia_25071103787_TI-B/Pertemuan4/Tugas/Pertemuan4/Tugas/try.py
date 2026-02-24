try:
    print(a)
except:
    print("Error.")

# Banyak exception
try:
    print(x)
except NameError:
    print("Variabel tidak terdefinisikan")
except:
    print("Terjadi kesalahan.")

# Else
x = False
try:
    print(x)
except:
    print("Tidak ada.")
else:
    print("Ada")