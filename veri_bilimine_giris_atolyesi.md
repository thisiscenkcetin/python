# Veri Bilimine Giriş Atölyesi

## Python Programlama - Hafta 1

**2 Saatlik Eğitim Materyali**

### 1. Atölye Hakkında

Bu atölye 6 hafta sürecek ve sizlere veri biliminin temellerini öğretmeyi hedefliyor. İlk haftamızda Python programlama dilinin temellerini öğreneceğiz. Python, veri bilimi dünyasının en popüler ve güçlü araçlarından biridir.

#### 1.1 Atölye İçeriği Özeti

- **Hafta 1:** Python Temelleri (Bugün)

- **Hafta 2:** Python ile OOP

- **Hafta 3:** NumPy ve  ile Veri Analizi

- **Hafta 4:** Pandas 

- **Hafta 5:** Veri Görselleştirme (Matplotlib, Seaborn)

- **Hafta 6:** Regresyon

### 2. Python Nedir?

Python, 1991 yılında Guido van Rossum tarafından geliştirilen, yüksek seviyeli, yorumlamalı ve genel amaçlı bir programlama dilidir. Okunabilirliği ve basit sözdizimi ile ünlüdür.

#### 2.1 Python'un Avantajları

- **Kolay Öğrenilir:** Basit ve okunabilir sözdizimi

- **Çok Yönlü:** Web geliştirme, veri bilimi, yapay zeka, otomasyon gibi birçok alanda kullanılır

- **Geniş Kütüphane Desteği:** NumPy, Pandas, Scikit-learn gibi güçlü kütüphaneler

- **Büyük Topluluk:** Milyonlarca geliştirici ve zengin kaynak

- **Açık Kaynak:** Ücretsiz ve sürekli gelişen

#### 2.2 Veri Biliminde Python

Python, veri bilimi alanında en çok tercih edilen dillerden biridir. Bunun başlıca nedenleri:

- Güçlü veri analizi kütüphaneleri (Pandas, NumPy)

- Makine öğrenimi framework'leri (TensorFlow, PyTorch, Scikit-learn)

- Veri görselleştirme araçları (Matplotlib, Seaborn, Plotly)

- Jupyter Notebook gibi interaktif geliştirme ortamları

### 3. Python Kurulumu ve Geliştirme Ortamları

#### 3.1 Python Kurulumu

- **Windows:** python.org adresinden Python 3.x sürümünü indirin ve yükleyin. Kurulum sırasında 'Add Python to PATH' seçeneğini işaretleyin.

- **macOS/Linux:** Genellikle Python önceden yüklüdür. Terminal'de 'python3 --version' komutu ile kontrol edin.

#### 3.2 Geliştirme Ortamları

| Araç | Açıklama |
| --- | --- |
| IDLE | Python ile birlikte gelen basit IDE |
| Jupyter Notebook | Veri bilimi için ideal, interaktif kod çalıştırma ortamı |
| VS Code | Microsoft'un güçlü ve popüler kod editörü |
| PyCharm | Profesyonel Python geliştirme için tam özellikli IDE |
| Google Colab | Bulut tabanlı, kurulum gerektirmeyen Jupyter ortamı |

**Tavsiye:** Başlangıç için Jupyter Notebook veya Google Colab kullanmanızı öneriyoruz.

### 4. İlk Python Programınız

#### 4.1 Hello World!

Geleneksel ilk program olan 'Hello World' ile başlayalım:

```python
print("Merhaba Dünya!")
```

**Çıktı:** Merhaba Dünya!

#### 4.2 Yorumlar

Yorumlar, kodunuzu açıklamak için kullanılır ve Python tarafından çalıştırılmaz:

```python
# Bu bir tek satırlık yorumdur
print("Merhaba") # Satır sonunda yorum

"""
Bu bir çok satırlı
yorumdur
"""
```

### 5. Değişkenler ve Veri Tipleri

#### 5.1 Değişken Tanımlama

Python'da değişken tanımlamak çok kolaydır. Tip belirtmenize gerek yoktur (dinamik tipleme):

```python
isim = "Ahmet"
yas = 25
boy = 1.75
ogrenci_mi = True
```

#### 5.2 Temel Veri Tipleri

| Tip | Açıklama | Örnek |
| --- | --- | --- |
| int | Tam sayılar | 42, -10, 0 |
| float | Ondalıklı sayılar | 3.14, -0.5, 2.0 |
| str | Metin (string) | "Python", 'Merhaba' |
| bool | Mantıksal değer | True, False |
| NoneType | Boş değer | None |

#### 5.3 Tip Dönüşümleri

Bir veri tipini başka bir tipe dönüştürebilirsiniz:

```python
sayi_str = "123"
sayi_int = int(sayi_str) # "123" -> 123
sayi_float = float(sayi_str) # "123" -> 123.0

yas = 25
yas_str = str(yas) # 25 -> "25"
```

#### 5.4 type() Fonksiyonu

Bir değişkenin tipini öğrenmek için `type()` fonksiyonunu kullanabilirsiniz:

```python
x = 42
print(type(x)) # <class 'int'>
```

### 6. Temel İşlemler

#### 6.1 Aritmetik İşlemler

| İşlem | Açıklama | Örnek |
| --- | --- | --- |
| + | Toplama | 5 + 3 = 8 |
| - | Çıkarma | 5 - 3 = 2 |
| * | Çarpma | 5 * 3 = 15 |
| / | Bölme | 10 / 3 = 3.33 |
| // | Tam bölme | 10 // 3 = 3 |
| % | Mod (kalan) | 10 % 3 = 1 |
| ** | Üs alma | 2 ** 3 = 8 |

#### 6.2 Karşılaştırma İşlemleri

```python
5 == 5 # True (eşit mi?)
5 != 3 # True (eşit değil mi?)
5 > 3 # True (büyük mü?)
5 < 3 # False (küçük mü?)
5 >= 5 # True (büyük veya eşit mi?)
5 <= 3 # False (küçük veya eşit mi?)
```

#### 6.3 Mantıksal İşlemler

```python
True and False # False (ve)
True or False # True (veya)
not True # False (değil)
```

### 7. String (Metin) İşlemleri

#### 7.1 String Oluşturma

```python
tek_tirnak = 'Merhaba'
cift_tirnak = "Dünya"
cok_satirli = """
Bu bir
çok satırlı
string'dir
"""
```

#### 7.2 String Birleştirme ve Tekrar

```python
isim = "Ahmet"
soyisim = "Yılmaz"
tam_isim = isim + " " + soyisim # "Ahmet Yılmaz"

tekrar = "Ha" * 3 # "HaHaHa"
```

#### 7.3 String Formatlama

```python
isim = "Mehmet"
yas = 30

# f-string (Python 3.6+, önerilen yöntem)
mesaj = f"Benim adım {isim} ve {yas} yaşındayım"

# format() metodu
mesaj = "Benim adım {} ve {} yaşındayım".format(isim, yas)
```

#### 7.4 Yararlı String Metotları

```python
metin = "Python Programlama"

metin.upper() # "PYTHON PROGRAMLAMA"
metin.lower() # "python programlama"
metin.title() # "Python Programlama"
metin.replace("Python", "Java") # "Java Programlama"
metin.split() # ['Python', 'Programlama']
len(metin) # 19 (uzunluk)
"Python" in metin # True
```

### 8. Kullanıcıdan Girdi Alma

`input()` fonksiyonu ile kullanıcıdan veri alabilirsiniz:

```python
isim = input("Adınız nedir? ")
print(f"Merhaba, {isim}!")

# Sayı almak için tip dönüşümü gerekir
yas = int(input("Yaşınız: "))
boy = float(input("Boyunuz (m): "))
```

### 9. Kontrol Yapıları (if/elif/else)

**Önemli:** Python'da girintileme (indentation) çok önemlidir! Kod bloklarını belirlemek için kullanılır.

#### 9.1 Basit if İfadesi

```python
yas = 18
if yas >= 18:
    print("Reşitsiniz")
```

#### 9.2 if-else İfadesi

```python
not_ortalmasi = 75
if not_ortalmasi >= 60:
    print("Geçtiniz!")
else:
    print("Kaldınız")
```

#### 9.3 if-elif-else İfadesi

```python
puan = 85
if puan >= 90:
    harf_notu = "AA"
elif puan >= 80:
    harf_notu = "BA"
elif puan >= 70:
    harf_notu = "BB"
elif puan >= 60:
    harf_notu = "CB"
else:
    harf_notu = "FF"

print(f"Harf notunuz: {harf_notu}")
```

### 10. Döngüler (Loops)

#### 10.1 for Döngüsü

`for` döngüsü, bir dizi üzerinde gezinmek için kullanılır:

```python
# 0'dan 4'e kadar sayıları yazdır
for i in range(5):
    print(i)
# Çıktı: 0, 1, 2, 3, 4

# Liste üzerinde gezinme
meyveler = ["elma", "armut", "muz"]
for meyve in meyveler:
    print(meyve)
```

**range() Fonksiyonu**

```python
range(5) # 0, 1, 2, 3, 4
range(2, 7) # 2, 3, 4, 5, 6
range(1, 10, 2) # 1, 3, 5, 7, 9 (adım=2)
```

#### 10.2 while Döngüsü

`while` döngüsü, bir koşul doğru olduğu sürece çalışır:

```python
sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1 # sayac = sayac + 1
# Çıktı: 0, 1, 2, 3, 4
```

**Dikkat:** `while` döngüsü sonsuz döngüye girmesin diye koşulun bir noktada `False` olacağından emin olun!

#### 10.3 break ve continue

```python
# break - döngüden çık
for i in range(10):
    if i == 5:
        break
    print(i) # 0, 1, 2, 3, 4

# continue - bu iterasyonu atla
for i in range(5):
    if i == 2:
        continue
    print(i) # 0, 1, 3, 4 (2 atlandı)
```

### 11. Veri Yapıları - Listeler

Listeler, birden fazla öğeyi saklamak için kullanılan sıralı ve değiştirilebilir koleksiyonlardır.

#### 11.1 Liste Oluşturma

```python
bos_liste = []
sayilar = [1, 2, 3, 4, 5]
meyveler = ["elma", "armut", "muz"]
karisik = [1, "iki", 3.0, True] # Farklı tipler
```

#### 11.2 Liste Elemanlarına Erişim

```python
meyveler = ["elma", "armut", "muz", "çilek"]
print(meyveler[0]) # "elma" (ilk eleman)
print(meyveler[-1]) # "çilek" (son eleman)
print(meyveler[1:3]) # ["armut", "muz"] (dilim)
```

#### 11.3 Liste Metotları

```python
sayilar = [1, 2, 3]
sayilar.append(4) # [1, 2, 3, 4] - sona ekle
sayilar.insert(0, 0) # [0, 1, 2, 3, 4] - başa ekle
sayilar.remove(2) # [0, 1, 3, 4] - 2'yi sil
son = sayilar.pop() # [0, 1, 3] - son elemanı çıkar
sayilar.sort() # Sırala
sayilar.reverse() # Tersine çevir
uzunluk = len(sayilar) # Liste uzunluğu
```

### 12. Fonksiyonlar

Fonksiyonlar, belirli bir görevi yerine getiren ve tekrar kullanılabilen kod bloklarıdır.

#### 12.1 Basit Fonksiyon

```python
def selamla():
    print("Merhaba!")

selamla() # Fonksiyonu çağır
```

#### 12.2 Parametreli Fonksiyon

```python
def selamla_kisi(isim):
    print(f"Merhaba, {isim}!")

selamla_kisi("Ahmet") # "Merhaba, Ahmet!"
```

#### 12.3 Değer Döndüren Fonksiyon

```python
def topla(a, b):
    sonuc = a + b
    return sonuc

toplam = topla(5, 3)
print(toplam) # 8
```

#### 12.4 Varsayılan Parametreler

```python
def us_al(sayi, us=2):
    return sayi ** us

print(us_al(3)) # 9 (3^2)
print(us_al(3, 3)) # 27 (3^3)
```

### 13. Nesne Yönelimli Programlama (OOP)

Nesne Yönelimli Programlama (Object-Oriented Programming), kodunuzu daha organize, yeniden kullanılabilir ve sürdürülebilir hale getiren bir programlama paradigmasıdır. Python, güçlü OOP desteği sunar.

#### 13.1 Sınıf (Class) ve Nesne (Object)

- **Sınıf:** Nesneler için bir şablon/taslaktır. Özellikleri ve davranışları tanımlar.

- **Nesne:** Sınıftan oluşturulan somut örneklerdir.

```python
# Basit bir sınıf tanımı
class Araba:
    pass # Boş sınıf

# Nesne oluşturma
araba1 = Araba()
```

#### 13.2 Constructor (__init__) ve Özellikler

Constructor (`__init__`), nesne oluşturulduğunda otomatik olarak çalışan özel bir metoddur. Nesnenin başlangıç özelliklerini tanımlar.

```python
class Ogrenci:
    def __init__(self, isim, yas, bolum):
        self.isim = isim
        self.yas = yas
        self.bolum = bolum

# Nesne oluşturma
ogrenci1 = Ogrenci("Ayşe", 20, "Bilgisayar Mühendisliği")
print(ogrenci1.isim) # "Ayşe"
print(ogrenci1.yas) # 20
```

#### 13.3 Metodlar (Methods)

Metodlar, sınıfın içinde tanımlanan fonksiyonlardır ve nesnelerin davranışlarını belirler.

```python
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0

    def hizlan(self, miktar):
        self.hiz += miktar
        print(f"Hız: {self.hiz} km/s")

    def yavasla(self, miktar):
        self.hiz -= miktar
        if self.hiz < 0:
            self.hiz = 0
        print(f"Hız: {self.hiz} km/s")

    def bilgi(self):
        return f"{self.yil} {self.marka} {self.model}"

# Kullanım
araba = Araba("Toyota", "Corolla", 2023)
print(araba.bilgi()) # "2023 Toyota Corolla"
araba.hizlan(50) # "Hız: 50 km/s"
araba.hizlan(30) # "Hız: 80 km/s"
araba.yavasla(20) # "Hız: 60 km/s"
```

#### 13.4 Kalıtım (Inheritance)

Kalıtım, bir sınıfın başka bir sınıftan özellik ve metodları miras almasını sağlar. Bu, kod tekrarını azaltır ve hiyerarşik yapılar oluşturmayı sağlar.

```python
# Ana sınıf (Parent/Base Class)
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def ses_cikar(self):
        print("Hayvan ses çıkarıyor...")

    def bilgi(self):
        return f"{self.isim}, {self.yas} yaşında"

# Alt sınıf (Child/Derived Class)
class Kopek(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas) # Ana sınıfın constructor'ını çağır
        self.cins = cins

    def ses_cikar(self): # Metodu override et
        print("Hav hav!")

    def getir(self): # Yeni metot
        print("Köpek topu getiriyor...")

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav!")

# Kullanım
kopek = Kopek("Karabaş", 3, "Golden Retriever")
print(kopek.bilgi()) # "Karabaş, 3 yaşında"
kopek.ses_cikar() # "Hav hav!"
kopek.getir() # "Köpek topu getiriyor..."

kedi = Kedi("Minnoş", 2)
kedi.ses_cikar() # "Miyav!"
```

#### 13.5 Kapsülleme (Encapsulation)

Kapsülleme, verileri ve metodları bir sınıfın içinde gizlemeyi ve dışarıdan erişimi kontrol etmeyi sağlar. Python'da alt çizgi (`_`) ile özel (private) özellikler tanımlanır.

```python
class BankaHesabi:
    def __init__(self, hesap_no, bakiye):
        self.hesap_no = hesap_no
        self.__bakiye = bakiye # Özel (private) özellik

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı")

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi")
        else:
            print("Yetersiz bakiye!")

    def bakiye_goster(self):
        return f"Bakiye: {self.__bakiye} TL"

# Kullanım
hesap = BankaHesabi("123456", 1000)
print(hesap.bakiye_goster()) # "Bakiye: 1000 TL"
hesap.para_yatir(500) # "500 TL yatırıldı"
hesap.para_cek(300) # "300 TL çekildi"
print(hesap.bakiye_goster()) # "Bakiye: 1200 TL"
```

#### 13.6 OOP'nin Temel Prensipleri

| Prensip | Açıklama |
| --- | --- |
| Kapsülleme | Verileri ve metodları bir arada tutma ve erişimi kontrol etme |
| Kalıtım | Bir sınıfın başka bir sınıftan özellik ve metot alması |
| Polimorfizm | Aynı arayüzün farklı şekillerde uygulanabilmesi (metot override) |
| Soyutlama | Karmaşık detayları gizleyerek basit bir arayüz sunma |

**Neden OOP Kullanmalıyız?**

- **Kod Yeniden Kullanılabilirliği:** Aynı kodu tekrar yazmadan kullanabilirsiniz

- **Modülerlik:** Kod daha organize ve yönetilebilir hale gelir

- **Bakım Kolaylığı:** Değişiklikler daha kolay yapılır

- **Gerçek Dünya Modelleme:** Nesneler gerçek hayattaki varlıkları temsil eder

### 14. Pratik Örnekler

#### 14.1 Örnek 1: Asal Sayı Kontrolü

```python
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

print(asal_mi(17)) # True
print(asal_mi(20)) # False
```

#### 14.2 Örnek 2: Listedeki En Büyük Sayı

```python
def en_buyuk_bul(liste):
    en_buyuk = liste[0]
    for sayi in liste:
        if sayi > en_buyuk:
            en_buyuk = sayi
    return en_buyuk

sayilar = [23, 45, 12, 89, 34]
print(en_buyuk_bul(sayilar)) # 89

# Ya da Python'un yerleşik max() fonksiyonu:
print(max(sayilar)) # 89
```

#### 14.3 Örnek 3: Fibonacci Serisi

```python
def fibonacci(n):
    seri = [0, 1]
    for i in range(2, n):
        sonraki = seri[i-1] + seri[i-2]
        seri.append(sonraki)
    return seri

print(fibonacci(10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### 15. Pratik Alıştırmalar

Bu alıştırmaları çözerek öğrendiklerinizi pekiştirin:

- **Alıştırma 1: Tek mi Çift mi?** Kullanıcıdan bir sayı alın ve bu sayının tek mi çift mi olduğunu ekrana yazdıran bir program yazın.

- **Alıştırma 2: Faktöriyel Hesaplama** Bir sayının faktöriyelini hesaplayan bir fonksiyon yazın. (Örnek: 5! = 5 × 4 × 3 × 2 × 1 = 120)

- **Alıştırma 3: Kelime Sayacı** Kullanıcıdan bir cümle alın ve bu cümlede kaç kelime olduğunu bulan bir program yazın.

- **Alıştırma 4: Ortalama Hesaplama** Bir liste içindeki sayıların ortalamasını hesaplayan bir fonksiyon yazın.

- **Alıştırma 5: Palindrom Kontrolü** Bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın. (Palindrom: tersten okunuşu da aynı olan kelime, örnek: 'kayak')

- **Alıştırma 6: Liste Filtreleme** Bir sayı listesinden sadece pozitif sayıları seçen bir fonksiyon yazın.

### 16. Gelecek Hafta için Hazırlık

- **Python.org:** Resmi Python dokümantasyonu

- **W3Schools Python Tutorial:** İnteraktif öğrenme platformu

- **Real Python:** Detaylı Python makaleleri ve öğreticiler

- **LeetCode / HackerRank:** Pratik yapabileceğiniz platformlar


