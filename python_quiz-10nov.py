"""
Python Alıştırmaları - 10.11.2025
Veri Bilimine Giriş Atölyesi
"""

import numpy as np

# 1) 0 ile 9 arasındaki tam sayılar
arr1 = np.arange(10)
print("1) 0-9 arası dizi:", arr1)

# 2) 3x4 sıfır matrisi
zeros_matrix = np.zeros((3, 4))
print("\n2) 3x4 sıfır matrisi:\n", zeros_matrix)

# 3) 2x3 birler matrisi
ones_matrix = np.ones((2, 3))
print("\n3) 2x3 birler matrisi:\n", ones_matrix)

# 4) reshape özellikleri
arr4 = np.arange(12).reshape(3, 4)
print("\n4) Boyut:", arr4.shape, "Eleman sayısı:", arr4.size, "Boyut sayısı:", arr4.ndim)

# 5) int64 dönüşümü
arr5 = np.array([10, 20, 30, 40], dtype=np.int64)
print("\n5) int64 dizisi:", arr5.dtype)

# 6) Koşullu seçim
arr6 = np.arange(20)
filtered = arr6[(arr6 > 5) & (arr6 < 15)]
print("\n6) 5-15 arası filtreleme:", filtered)

# 7-8) Vektör işlemleri
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\n7-8) Toplam:", a + b, "Çarpım:", a * b)

# 9-10) Matris indeksleme
M = np.arange(1, 26).reshape(5, 5)
print("\n9) Matris:\n", M)
print("10) 2. satır:", M[1], "3. sütun:", M[:, 2])

# 11-12) Transpose
mat = np.random.randint(0, 10, (3, 2))
print("\n12) Orijinal (3x2):\n", mat)
print("Transpose (2x3):\n", mat.T)

# 13-14) NaN yönetimi
dizi = np.array([1, 2, np.nan, 4, 5, np.nan, 7])
nan_count = np.isnan(dizi).sum()
print("\n14) NaN sayısı:", nan_count)

# 15-16) İstatistiksel hesaplar
mat5x5 = np.random.randint(0, 100, (5, 5))
print("\n16) Ortalama:", mat5x5.mean(), "Max:", mat5x5.max(), "Sütun std:", mat5x5.std(axis=0))

# 17) Birleştirme
a = np.array([1, 2])
b = np.array([3, 4])
print("\n17) Yatay:", np.hstack((a, b)), "Dikey:\n", np.vstack((a, b)))

# 18-19) Matris çarpımı
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\n19) Matris çarpımı:\n", np.dot(A, B))

# 20-21) Veri merkezleme
mat_centered = np.random.rand(5, 5)
mat_centered = mat_centered - mat_centered.mean(axis=0)
print("\n21) Merkezlenmiş matris ortalamaları:", mat_centered.mean(axis=0))

# 22-24) Determinant ve ters matris
C = np.array([[4, 7], [2, 6]])
det = np.linalg.det(C)
inv = np.linalg.inv(C)
identity_check = np.dot(C, inv)
print("\n24) Determinant:", det, "Ters matris:\n", inv, "Doğrulama:\n", identity_check)

# 25) Benzersiz elemanlar
veri = np.array([1, 2, 1, 4, 5, 2, 7, 1])
unique, counts = np.unique(veri, return_counts=True)
print("\n25) Benzersiz:", unique, "Sayılar:", counts)

# 26-27) Kırpma işlemi
dizi = np.random.randn(100)
clipped = np.clip(dizi, -2, 2)
print("\n27) Kırpılmış min/max:", clipped.min(), clipped.max())

# 28-29) Vektör çarpımları
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("\n29) Nokta çarpım:", np.dot(v1, v2), "Dış çarpım:\n", np.outer(v1, v2))

# 30) Performans karşılaştırması
py_list = list(range(1000000))
np_array = np.arange(1000000)
print("\n30) NumPy dizisi boyutu:", np_array.nbytes, "bayt")

# Tensör İşlemleri
print("\n" + "="*50 + "\nTensör İşlemleri\n" + "="*50)

# Eksen tabanlı filtreleme
tensor = np.random.rand(5, 20, 8)
time_means = tensor.mean(axis=(0, 2))
global_mean = tensor.mean()
broadcasted = tensor - global_mean
print("Zaman ortalamaları şekli:", time_means.shape)
print("Yayınlanmış tensör şekli:", broadcasted.shape)

# Öklid uzaklığı
A = np.random.rand(50, 4)
B = np.random.rand(1, 4)
distances = np.sqrt(((A - B)**2).sum(axis=1))
min_index = np.argmin(distances)
print("\nEn yakın nokta indeksi:", min_index)

# Finansal volatilite
prices = np.random.rand(120, 6) * 100
returns = np.diff(prices, axis=0) / prices[:-1]
cov_matrix = np.cov(returns.T)
eigenvals, eigenvecs = np.linalg.eig(cov_matrix)
min_eigenvec = eigenvecs[:, np.argmin(eigenvals)]
print("\nEn küçük özdeğerli vektör:", min_eigenvec)

# 2D evrişim
image = np.random.rand(20, 20)
kernel = np.full((3, 3), 1/9)
output = np.zeros((18, 18))
for i in range(18):
    for j in range(18):
        output[i,j] = np.sum(image[i:i+3, j:j+3] * kernel)
print("\nEvrişim çıktısı şekli:", output.shape)

# İklim anomalileri
climate = np.random.rand(10, 30, 2)
means = climate.mean(axis=(0,1)).reshape(1,1,2)
anomalies = climate - means
print("\nAnomali tensörü şekli:", anomalies.shape)

# Çoklu eksen sıralama
scores = np.random.randint(0, 100, (100, 3))
sorted_indices = np.lexsort((scores[:,0], -scores[:,2]))
top10 = scores[sorted_indices[:10]]
print("\nEn iyi 10 öğrenci:\n", top10)

# Gruplama ve persentil
data = np.random.rand(1000)
split_indices = [50, 150, 300, 500]
groups = np.array_split(data, split_indices)
percentiles = [np.percentile(g, 90) for g in groups if len(g) > 0]
print("\nGrupların %90 persentili:", percentiles)

# Matris birleştirme ve çarpım
A = np.random.rand(5, 10)
B = np.random.rand(5, 10)
C = np.random.rand(10, 10)
stacked = np.stack((A, B))
result = np.dot(stacked.reshape(10, 10), C)
print("\nBirleştirilmiş çarpım şekli:", result.shape)

# NaN doldurma
data = np.random.rand(20, 5)
nan_indices = np.random.choice(400, 10, replace=False)
data.flat[nan_indices] = np.nan
col_medians = np.nanmedian(data, axis=0)
filled = np.where(np.isnan(data), col_medians, data)
print("\nNaN doldurma başarılı:", not np.any(np.isnan(filled)))

# Özel birleştirme
A = np.random.rand(10, 3)
B = np.random.rand(10, 3)
combined = np.column_stack((A[:,0], B[:,1], A[:,2]))
stats = [np.median(combined[:,0]), np.std(combined[:,1]), np.sum(combined[:,2])]
print("\nBirleştirilmiş istatistikler:", stats)


## Mesaj
print("\nHocam,")
print("Ödevin birini yapamadan, diğeri geliyor")
print("https://www.youtube.com/watch?v=zA1HxqAg1HU")
print("Bittik hocam (:")
