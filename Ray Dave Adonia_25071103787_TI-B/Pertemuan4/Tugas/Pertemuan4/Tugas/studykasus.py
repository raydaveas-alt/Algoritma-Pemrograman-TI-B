def soal(x, y):
    print(f"Apa hasil dari... {x} x {y}?")
    percobaan = 0
    
    while percobaan < 3:
        print("Percobaan yang tersisa:", 3 - percobaan)
        try:
            cek = int(input("Jawab: "))
        
            if cek != x * y:
                raise Exception
            else:
                print("Benar.")
            return

        except:
            print("Salah.")
            percobaan += 1
        
    
    print("Pertanyaan selesai.")

soal(5, 6)