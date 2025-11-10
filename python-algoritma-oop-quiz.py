"""
Python Algoritma&OOP Alıştırmaları
Veri Bilimine Giriş Atölyesi
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict
import math


# KOLAY SEVİYE SORULAR

# SORU 1: Öğrenci Sınıfı
class Ogrenci:
    def __init__(self, isim, ogrenci_no):
        self.isim = isim
        self.ogrenci_no = ogrenci_no
        self.__notlar = []
    
    def not_ekle(self, not_degeri):
        if 0 <= not_degeri <= 100:
            self.__notlar.append(not_degeri)
            print(f"✅ {not_degeri} notu eklendi")
            return True
        else:
            print(f"❌ Hata: Not 0-100 arasında olmalı!")
            return False
    
    def ortalama_hesapla(self):
        if not self.__notlar:
            return 0
        return sum(self.__notlar) / len(self.__notlar)
    
    def bilgileri_goster(self):
        ortalama = self.ortalama_hesapla()
        print(f"Öğrenci: {self.isim} ({self.ogrenci_no})")
        print(f"Notlar: {self.__notlar}")
        print(f"Ortalama: {ortalama:.2f}")
    
    def get_notlar(self):
        return self.__notlar.copy()


# SORU 2: Hesap Makinesi
class HesapMakinesi:
    def __init__(self):
        self.__bellek = 0
    
    @staticmethod
    def topla(a, b):
        return a + b
    
    @staticmethod
    def cikar(a, b):
        return a - b
    
    @staticmethod
    def carp(a, b):
        return a * b
    
    @staticmethod
    def bol(a, b):
        if b == 0:
            raise ValueError("Hata: Sıfıra bölme mümkün değil!")
        return a / b
    
    def bellek_kaydet(self, deger):
        self.__bellek = deger
        print(f"✅ {deger} belleğe kaydedildi")
    
    def bellek_cagir(self):
        return self.__bellek
    
    def bellek_temizle(self):
        self.__bellek = 0
        print("✅ Bellek temizlendi")


# SORU 3: Kitap Sınıfı
class Kitap:
    def __init__(self, baslik, yazar, sayfa_sayisi):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.__okunan_sayfa = 0
    
    def sayfa_oku(self, sayfa_sayisi):
        if sayfa_sayisi <= 0:
            print("❌ Sayfa sayısı pozitif olmalı!")
            return
        
        yeni_okunan = self.__okunan_sayfa + sayfa_sayisi
        
        if yeni_okunan >= self.sayfa_sayisi:
            self.__okunan_sayfa = self.sayfa_sayisi
            print("✅ Kitap tamamlandı!")
        else:
            self.__okunan_sayfa = yeni_okunan
            print(f"{sayfa_sayisi} sayfa okundu. Toplam: {self.__okunan_sayfa}/{self.sayfa_sayisi}")
    
    def sayfa_atla(self, sayfa_sayisi):
        yeni_okunan = min(self.__okunan_sayfa + sayfa_sayisi, self.sayfa_sayisi)
        self.__okunan_sayfa = yeni_okunan
    
    def tamamlandi_mi(self):
        return self.__okunan_sayfa >= self.sayfa_sayisi
    
    def kalan_sayfa(self):
        return self.sayfa_sayisi - self.__okunan_sayfa
    
    def __str__(self):
        durum = "Tamamlandı" if self.tamamlandi_mi() else f"{self.kalan_sayfa()} sayfa kaldı"
        return f"'{self.baslik}' by {self.yazar} - {self.sayfa_sayisi} sayfa ({durum})"


# SORU 4: Banka Hesabı
class BankaHesabi:
    def __init__(self, hesap_no, sahip, baslangic_bakiye=0):
        self.hesap_no = hesap_no
        self.sahip = sahip
        self.__bakiye = baslangic_bakiye
        self.__islem_gecmisi = []
    
    def para_yatir(self, tutar):
        if tutar <= 0:
            print("❌ Tutar pozitif olmalı!")
            return False
        
        self.__bakiye += tutar
        self.__islem_gecmisi.append(f"+{tutar} TL yatırıldı")
        print(f"✅ {tutar} TL yatırıldı. Yeni bakiye: {self.__bakiye} TL")
        return True
    
    def para_cek(self, tutar):
        if tutar <= 0:
            print("❌ Tutar pozitif olmalı!")
            return False
        
        if tutar > self.__bakiye:
            print("❌ Yetersiz bakiye!")
            return False
        
        self.__bakiye -= tutar
        self.__islem_gecmisi.append(f"-{tutar} TL çekildi")
        print(f"✅ {tutar} TL çekildi. Yeni bakiye: {self.__bakiye} TL")
        return True
    
    def bakiye_sorgula(self):
        return self.__bakiye
    
    def islem_gecmisi_goster(self):
        print(f"Hesap No: {self.hesap_no} - {self.sahip}")
        print("İşlem Geçmişi:")
        for islem in self.__islem_gecmisi:
            print(f"  {islem}")
        print(f"Güncel Bakiye: {self.__bakiye} TL")


# SORU 5: Geometrik Şekiller
class Sekil(ABC):
    @abstractmethod
    def alan_hesapla(self):
        pass
    
    @abstractmethod
    def cevre_hesapla(self):
        pass


class Dikdortgen(Sekil):
    def __init__(self, genislik, yukseklik):
        if genislik <= 0 or yukseklik <= 0:
            raise ValueError("Boyutlar pozitif olmalı!")
        self.genislik = genislik
        self.yukseklik = yukseklik
    
    def alan_hesapla(self):
        return self.genislik * self.yukseklik
    
    def cevre_hesapla(self):
        return 2 * (self.genislik + self.yukseklik)
    
    def __str__(self):
        return f"Dikdörtgen({self.genislik}x{self.yukseklik})"


class Daire(Sekil):
    def __init__(self, yaricap):
        if yaricap <= 0:
            raise ValueError("Yarıçap pozitif olmalı!")
        self.yaricap = yaricap
    
    def alan_hesapla(self):
        return math.pi * (self.yaricap ** 2)
    
    def cevre_hesapla(self):
        return 2 * math.pi * self.yaricap
    
    def __str__(self):
        return f"Daire(r={self.yaricap})"


# ORTA SEVİYE SORULAR

# SORU 6: Çalışan Yönetim Sistemi
class Calisan(ABC):
    def __init__(self, isim, maas, departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    
    @abstractmethod
    def maas_hesapla(self):
        pass
    
    def bilgileri_goster(self):
        hesaplanan = self.maas_hesapla()
        print(f"{self.isim} - {self.departman}, Maaş: {hesaplanan} TL")


class NormalCalisan(Calisan):
    def maas_hesapla(self):
        return self.maas


class Yonetici(Calisan):
    def __init__(self, isim, maas, departman, ekip_buyuklugu):
        super().__init__(isim, maas, departman)
        self.ekip_buyuklugu = ekip_buyuklugu
    
    def maas_hesapla(self):
        if self.ekip_buyuklugu >= 10:
            bonus = self.maas * 0.30
        elif self.ekip_buyuklugu >= 5:
            bonus = self.maas * 0.20
        else:
            bonus = self.maas * 0.10
        return self.maas + bonus


class Muhendis(Calisan):
    def __init__(self, isim, maas, departman, proje_sayisi=0):
        super().__init__(isim, maas, departman)
        self.proje_sayisi = proje_sayisi
    
    def maas_hesapla(self):
        return self.maas + (self.proje_sayisi * 1000)


# SORU 7: Kütüphane Sistemi
class KitapDurumu(Enum):
    MEVCUT = "Mevcut"
    ODUNC_VERILMIS = "Ödünç Verilmiş"


class KitapKutuphane:
    def __init__(self, baslik, yazar):
        self.baslik = baslik
        self.yazar = yazar
        self.durum = KitapDurumu.MEVCUT
        self.odunc_alan = None
    
    def odunc_ver(self, uye):
        if self.durum == KitapDurumu.MEVCUT:
            self.durum = KitapDurumu.ODUNC_VERILMIS
            self.odunc_alan = uye
            return True
        return False
    
    def iade_et(self):
        self.durum = KitapDurumu.MEVCUT
        self.odunc_alan = None


class UyeKutuphane:
    def __init__(self, isim, uye_no, max_kitap=3):
        self.isim = isim
        self.uye_no = uye_no
        self.max_kitap = max_kitap
        self.alinan_kitaplar = []
    
    def kitap_alabilir_mi(self):
        return len(self.alinan_kitaplar) < self.max_kitap


class Kutuphane:
    def __init__(self, isim):
        self.isim = isim
        self.kitaplar = []
        self.uyeler = []
    
    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
    
    def uye_ekle(self, uye):
        self.uyeler.append(uye)
    
    def odunc_ver(self, kitap, uye):
        if uye.kitap_alabilir_mi() and kitap.odunc_ver(uye):
            uye.alinan_kitaplar.append(kitap)
            print(f"✅ {kitap.baslik} kitabı {uye.isim}'e verildi")
            return True
        print(f"❌ Kitap verilemedi")
        return False


# SORU 8: Ev Otomasyon Sistemi
class Cihaz(ABC):
    def __init__(self, isim, konum):
        self.isim = isim
        self.konum = konum
        self.acik = False
    
    def ac(self):
        self.acik = True
        print(f"✅ {self.isim} açıldı")
    
    def kapat(self):
        self.acik = False
        print(f"✅ {self.isim} kapatıldı")
    
    @abstractmethod
    def durum_bilgisi(self):
        pass


class Isik(Cihaz):
    def __init__(self, isim, konum):
        super().__init__(isim, konum)
        self.parlaklik = 50
    
    def parlaklik_ayarla(self, deger):
        self.parlaklik = max(0, min(100, deger))
        print(f"{self.isim} parlaklığı: {self.parlaklik}%")
    
    def durum_bilgisi(self):
        return f"{self.isim} ({'Açık' if self.acik else 'Kapalı'}), Parlaklık: {self.parlaklik}%"


class Termostat(Cihaz):
    def __init__(self, isim, konum):
        super().__init__(isim, konum)
        self.hedef_sicaklik = 22
    
    def sicaklik_ayarla(self, derece):
        self.hedef_sicaklik = max(10, min(35, derece))
        print(f" {self.isim} hedef sıcaklık: {self.hedef_sicaklik}°C")
    
    def durum_bilgisi(self):
        return f"{self.isim} ({'Açık' if self.acik else 'Kapalı'}), Hedef: {self.hedef_sicaklik}°C"


# SORU 9: E-ticaret Sepet Sistemi
class Urun:
    def __init__(self, isim, fiyat, stok):
        self.isim = isim
        self.fiyat = fiyat
        self.stok = stok
    
    def stok_kontrol(self, miktar):
        return self.stok >= miktar
    
    def stok_azalt(self, miktar):
        if self.stok_kontrol(miktar):
            self.stok -= miktar
            return True
        return False


class SepetOgesi:
    def __init__(self, urun, miktar):
        self.urun = urun
        self.miktar = miktar
    
    def toplam_fiyat(self):
        return self.urun.fiyat * self.miktar


class Sepet:
    def __init__(self):
        self.ogeler = []
        self.indirim_orani = 0
    
    def urun_ekle(self, urun, miktar):
        if urun.stok_kontrol(miktar):
            self.ogeler.append(SepetOgesi(urun, miktar))
            print(f"✅ {miktar}x {urun.isim} sepete eklendi")
            return True
        print(f"❌ Yetersiz stok!")
        return False
    
    def toplam_hesapla(self):
        toplam = sum(oge.toplam_fiyat() for oge in self.ogeler)
        indirim = toplam * self.indirim_orani
        return toplam - indirim
    
    def indirim_uygula(self, oran):
        self.indirim_orani = oran
        print(f"✅ %{oran*100} indirim uygulandı")
    
    def ozet_goster(self):
        print("\n SEPET ÖZETİ:")
        for oge in self.ogeler:
            print(f"  {oge.miktar}x {oge.urun.isim} - {oge.toplam_fiyat()} TL")
        print(f"Toplam: {self.toplam_hesapla():.2f} TL")


# SORU 10: Veri Analiz Aracı
class VeriAnalizci:
    def __init__(self):
        self.veri = []
    
    def veri_yukle(self, liste):
        self.veri = liste
        print(f"✅ {len(liste)} veri yüklendi")
    
    def ortalama(self):
        if not self.veri:
            return 0
        return sum(self.veri) / len(self.veri)
    
    def medyan(self):
        if not self.veri:
            return 0
        sirali = sorted(self.veri)
        n = len(sirali)
        if n % 2 == 0:
            return (sirali[n//2-1] + sirali[n//2]) / 2
        return sirali[n//2]
    
    def standart_sapma(self):
        if not self.veri:
            return 0
        ort = self.ortalama()
        varyans = sum((x - ort) ** 2 for x in self.veri) / len(self.veri)
        return varyans ** 0.5
    
    def rapor_olustur(self):
        print("\n VERİ ANALİZ RAPORU:")
        print(f"Veri Sayısı: {len(self.veri)}")
        print(f"Ortalama: {self.ortalama():.2f}")
        print(f"Medyan: {self.medyan():.2f}")
        print(f"Standart Sapma: {self.standart_sapma():.2f}")
        print(f"Min: {min(self.veri) if self.veri else 0}")
        print(f"Max: {max(self.veri) if self.veri else 0}")


# TEST KODLARI
# ‿‿‿‿‿‿‿‿⁣⁣‿‿⁣‿‿⁣‿‿⁣‿⁣‿⁣‿

if __name__ == "__main__":
    print("="*70)
    print("PYTHON OOP ALIŞTIRMALARI")
    print("="*70)
    
    # Öğrenci testi
    print("\n--- Öğrenci Sınıfı Testi ---")
    ogrenci1 = Ogrenci("Ali Veli", "12345")
    ogrenci1.not_ekle(85)
    ogrenci1.not_ekle(90)
    ogrenci1.not_ekle(78)
    ogrenci1.bilgileri_goster()
    
    # Hesap makinesi testi
    print("\n--- Hesap Makinesi Testi ---")
    calc = HesapMakinesi()
    print(f"10 + 5 = {calc.topla(10, 5)}")
    print(f"10 * 5 = {calc.carp(10, 5)}")
    calc.bellek_kaydet(42)
    print(f"Bellekteki değer: {calc.bellek_cagir()}")
    
    # Kitap testi
    print("\n--- Kitap Sınıfı Testi ---")
    kitap1 = Kitap("Python Programlama", "Ali Veli", 300)
    print(kitap1)
    kitap1.sayfa_oku(100)
    kitap1.sayfa_oku(150)
    print(kitap1)
    
    # Banka hesabı testi
    print("\n--- Banka Hesabı Testi ---")
    hesap1 = BankaHesabi("12345", "Ahmet Yılmaz", 1000)
    hesap1.para_yatir(500)
    hesap1.para_cek(300)
    hesap1.islem_gecmisi_goster()
    
    # Geometrik şekiller testi
    print("\n--- Geometrik Şekiller Testi ---")
    sekiller = [Dikdortgen(5, 3), Daire(4)]
    for sekil in sekiller:
        print(f"{sekil}: Alan={sekil.alan_hesapla():.2f}, Çevre={sekil.cevre_hesapla():.2f}")
    
    print("\n" + "="*70)
    print("TESTLER TAMAMLANDI!")
    print("="*70)


