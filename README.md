---

# Python Projeleri: Yapılacaklar Listesi, Banka Sistemi ve Kütüphane Yönetimi

Bu repo, Python ile geliştirilmiş üç temel projeyi içermektedir. Projeler, farklı uygulama senaryolarını modelleyerek nesne yönelimli programlama (OOP) konseptlerini öğrenmek ve geliştirmek için tasarlanmıştır.

---

## Projeler

### 1. **Yapılacaklar Listesi (To-Do List)**

#### Özellikler:
- Görev ekleme.
- Görev tamamlama ve tamamlandı olarak işaretleme.
- Görev listeleme (tamamlananlar ve tamamlanmayanlar ayrı tutulur).
- Görev silme.
- Görevleri bir `.txt` dosyasına kaydetme ve program başlatıldığında yeniden yükleme.

#### Kullanılan Sınıflar:
- **`Task`**:  
  Görev adı ve tamamlanma durumunu saklar. Görevi tamamlanmış olarak işaretlemek için metot içerir.
- **`TaskManager`**:  
  Görevlerin eklenmesi, silinmesi ve yönetilmesi için gerekli metotları sağlar. Görevleri `.txt` dosyasına kaydeder ve yükler.

#### Kullanım:
Program çalıştırıldığında kullanıcı menü yardımıyla görev ekleyebilir, tamamlayabilir, silebilir ve listeleyebilir. Tüm görevler otomatik olarak dosyaya kaydedilir ve program yeniden çalıştırıldığında yüklenir.

---

### 2. **Basit Banka Sistemi**

#### Özellikler:
- Kullanıcı hesap açma.
- Para yatırma ve çekme işlemleri.
- Hesap bakiyesi sorgulama.
- Birden fazla kullanıcıyı yönetme.

#### Kullanılan Sınıflar:
- **`Kullanici`**:  
  Hesap adı, hesap numarası ve bakiyeyi tutar. Para yatırma ve çekme işlemleri için metot içerir.
- **`Banka`**:  
  Kullanıcı hesaplarının oluşturulması ve işlemlerinin yönetilmesini sağlar. Hesap numarasına göre işlem yapma kontrolü ekler.

#### Kullanım:
Kullanıcılar hesap açabilir, para yatırabilir, çekebilir ve bakiyelerini sorgulayabilir. Tüm işlemler hesap numarası üzerinden gerçekleştirilir.

---

### 3. **Kütüphane Yönetim Sistemi**

#### Özellikler:
- Kitap ekleme.
- Kitapları listeleme (ödünç alınan ve müsait olanlar dahil).
- Kitap ödünç verme ve geri alma.

#### Kullanılan Sınıflar:
- **`Kitap`**:  
  Kitap adı, yazar adı ve ödünç durumu bilgilerini tutar. Ödünç verme ve geri alma işlemleri için metotlar içerir.
- **`Kutuphane`**:  
  Kitap ekleme, listeleme, ödünç verme ve geri alma işlemlerini yönetir.

#### Kullanım:
Kullanıcı, kitap ekleyebilir, kitapları listeleyebilir, ödünç alabilir ve geri verebilir. Her işlem kitap listesinden seçim yapılarak gerçekleştirilir.

---

## Kullanım Talimatları

1. Her proje, ilgili Python dosyasında bir `main()` fonksiyonuna sahiptir.
2. Dosyayı çalıştırarak projeyi başlatabilirsiniz.
3. Kullanıcı dostu menüler yardımıyla işlemleri gerçekleştirebilirsiniz.

---

## Geliştirme Önerileri

### Yapılacaklar Listesi:
- Görevleri tarih veya öncelik sırasına göre sıralama.
- Tamamlanma durumunu renklendirme veya görselleştirme.

### Banka Sistemi:
- Kullanıcılar arasında para transferi ekleme.
- Hesap işlem geçmişini görüntüleme.

### Kütüphane Sistemi:
- Kitap silme özelliği.
- Kütüphane envanterini dışa aktarma (ör. bir `.csv` dosyasına).

---
