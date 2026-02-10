def rata_rata(nilai):
    if not nilai:
        return "Data kosong."
    return sum(nilai) / len(nilai)

print(rata_rata([80, 75, 90, 60, 85]))