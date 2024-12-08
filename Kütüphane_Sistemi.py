# Kitap Sınıfı
class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi = False

    def odunc_ver(self):
        if not self.odunc_alindi:
            self.odunc_alindi = True
            print(f"'{self.ad}' kitabı ödünç verildi.")
        else:
            print(f"'{self.ad}' kitabı zaten ödünç alınmış!")

    def geri_al(self):
        if self.odunc_alindi:
            self.odunc_alindi = False
            print(f"'{self.ad}' kitabı geri alındı.")
        else:
            print(f"'{self.ad}' kitabı zaten kütüphanede!")

    def __str__(self):
        status = "Ödünçte" if self.odunc_alindi else "Müsait"
        return f"{self.ad} - {self.yazar} [{status}]"

# Kütüphane Sınıfı
class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, ad, yazar):
        yeni_kitap = Kitap(ad, yazar)
        self.kitaplar.append(yeni_kitap)
        print(f"'{ad}' kitabı kütüphaneye eklendi.")

    def kitaplari_listele(self):
        print("\nKütüphanedeki Kitaplar:")
        for i, kitap in enumerate(self.kitaplar):
            print(f"{i}. {kitap}")
        print()

    def odunc_ver(self, index):
        try:
            kitap = self.kitaplar[index]
            kitap.odunc_ver()
        except IndexError:
            print("Geçersiz kitap numarası!")

    def geri_al(self, index):
        try:
            kitap = self.kitaplar[index]
            kitap.geri_al()
        except IndexError:
            print("Geçersiz kitap numarası!")

# Ana Program
def main():
    kutuphane = Kutuphane()

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ödünç Ver")
        print("4. Kitap Geri Al")
        print("5. Çıkış")
        secim = input("Seçiminizi yapın: ")
    
        if secim == "1":
            ad = input("Kitap Adı: ")
            yazar = input("Yazar Adı: ")
            kutuphane.kitap_ekle(ad, yazar)
        elif secim == "2":
            kutuphane.kitaplari_listele()
        elif secim == "3":
            kutuphane.kitaplari_listele()
            index = int(input("Ödünç verilecek kitabın numarası: "))
            kutuphane.odunc_ver(index)
        elif secim == "4":
            kutuphane.kitaplari_listele()
            index = int(input("Geri alınacak kitabın numarası: "))
            kutuphane.geri_al(index)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    main()
