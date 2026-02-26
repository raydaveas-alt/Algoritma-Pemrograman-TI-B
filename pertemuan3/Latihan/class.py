class Kucing:
    def __init__(self, nama, jk, jenis, warna, umur, lokasi, meong):
        self.nama = nama
        self.jk = jk
        self.jenis = jenis
        self.warna = warna
        self.umur = umur
        self.lokasi = lokasi
        self.meong = meong

    def perkenalan(self):
        print(f"Namanya {self.nama}, umurnya {self.umur} tahun")

    def bio(self):
        print(f"{self.nama} adalah kucing {self.jenis} {self.jk} yang ada di {self.lokasi}.")

    def biolengkap(self):
        print(f"{self.nama} adalah kucing {self.jenis} {self.jk} berusia {self.umur} tahun yang berada di {self.lokasi}. {self.meong}.")

    def rcta(self):
        if self.lokasi == "Indonesia":
            self.meong = "Meong"
        elif self.lokasi == "Serbia":
            self.meong = "Мијау"
        elif self.lokasi == "Mesir":
            self.meong = "مواء"
        elif self.lokasi == "Thailand":
            self.meong = "เหมียว"
        else:
            self.meong = "Meow"
        print(f"{self.nama} sudah dipindahkan ke {self.lokasi}. {self.meong}.")

k1 = Kucing("Oyen", "jantan", "Persia", "coklat", 0, "Indonesia", "Meong")
k2 = Kucing("Mpus", "betina", "Kampung", "coklat", 1, "Indonesia", "Meong")
k3 = Kucing("Pushok", "jantan", "Siberia", "krim", 1, "Serbia", "Мијау")
k4 = Kucing("Qamar", "jantan", "Ragdoll", "abu-abu", 5, "Mesir", "مواء")
k5 = Kucing("Waan", "betina", "Siam", "putih", 7, "Thailand", "เหมียว")
k1.perkenalan()
k2.bio()
print()

print("Sebelum diubah.")
k1.biolengkap()
k2.biolengkap()
k3.biolengkap()
k4.biolengkap()
k5.biolengkap()
print()


print("setelah diubah")
k4.lokasi = "Indonesia"
k4.biolengkap()
k4.rcta()
k1.lokasi = "Serbia"
k1.rcta()