import math

# Fungsi Menghitung Peluang Muncul Pada Dadu
def peluangDadu (banyakdadu , matadadu, maximalmatadadu):
    return (maximalmatadadu * banyakdadu / matadadu) / banyakdadu  * 100

# Fungsi Menghitung Peluang Munculnya suatu Bola dalam pengambilan acak
def peluangBola (hijau, hitam, merah, carihijau, carihitam, carimerah):
    return ((carihijau + carihitam + carimerah) / (hijau + hitam + merah)) * 100

# Fungsi Menghitung Peluang Munculnya suatu angka
def peluangAngka (banyakangka, banyakangkacari):
    return (banyakangkacari / banyakangka) * 100
