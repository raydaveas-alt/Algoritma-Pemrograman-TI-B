def bilangan_prima(n):
    hasil = []
    for angka in range(2, n + 1):
        prima = True
        for i in range(2, angka):
            if angka % i == 0:
                prima = False
                break
        if prima:
            hasil.append(angka)
    return hasil

hasil_prima = bilangan_prima(50)
hasil_prima.append(50)
print(hasil_prima)
