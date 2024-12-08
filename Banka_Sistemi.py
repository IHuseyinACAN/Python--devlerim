# Kullanıcı Sınıfı
class Kullanici:
    def __init__(self, ad, hesap_numarasi, bakiye=0.0):
        self.ad = ad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Geçerli bir miktar girin.")

    def para_cek(self, miktar):
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL başarıyla çekildi. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar!")

    def bakiye_goster(self):
        print(f"Hesap Adı: {self.ad}, Hesap Numarası: {self.hesap_numarasi}, Bakiye: {self.bakiye} TL")

# Banka Sınıfı
class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_olustur(self, ad, hesap_numarasi, baslangic_bakiyesi=0.0):
        if hesap_numarasi in self.kullanicilar:
            print("Bu hesap numarası zaten mevcut!")
        else:
            self.kullanicilar[hesap_numarasi] = Kullanici(ad, hesap_numarasi, baslangic_bakiyesi)
            print(f"{ad} için hesap oluşturuldu. Hesap Numarası: {hesap_numarasi}, Başlangıç Bakiyesi: {baslangic_bakiyesi} TL")

    def kullanici_bul(self, hesap_numarasi):
        return self.kullanicilar.get(hesap_numarasi, None)

    def para_yatir(self, hesap_numarasi, miktar):
        kullanici = self.kullanici_bul(hesap_numarasi)
        if kullanici:
            kullanici.para_yatir(miktar)
        else:
            print("Hesap bulunamadı!")

    def para_cek(self, hesap_numarasi, miktar):
        kullanici = self.kullanici_bul(hesap_numarasi)
        if kullanici:
            kullanici.para_cek(miktar)
        else:
            print("Hesap bulunamadı!")

    def bakiye_sorgula(self, hesap_numarasi):
        kullanici = self.kullanici_bul(hesap_numarasi)
        if kullanici:
            kullanici.bakiye_goster()
        else:
            print("Hesap bulunamadı!")

# Ana Program
def main():
    banka = Banka()

    while True:
        print("\n1. Hesap Oluştur")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Bakiye Sorgula")
        print("5. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Hesap Adı: ")
            hesap_numarasi = input("Hesap Numarası: ")
            baslangic_bakiyesi = float(input("Başlangıç Bakiyesi: "))
            banka.hesap_olustur(ad, hesap_numarasi, baslangic_bakiyesi)
        elif secim == "2":
            hesap_numarasi = input("Hesap Numarası: ")
            miktar = float(input("Yatırılacak Miktar: "))
            banka.para_yatir(hesap_numarasi, miktar)
        elif secim == "3":
            hesap_numarasi = input("Hesap Numarası: ")
            miktar = float(input("Çekilecek Miktar: "))
            banka.para_cek(hesap_numarasi, miktar)
        elif secim == "4":
            hesap_numarasi = input("Hesap Numarası: ")
            banka.bakiye_sorgula(hesap_numarasi)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    main()
