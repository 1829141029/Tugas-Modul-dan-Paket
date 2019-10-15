import Peluang

def main ():
    # Dadu
    banyakdadu = 2
    matadadu = 6
    maximalmatadadu = 2

    Hasilpeluang = Peluang.peluangDadu(banyakdadu , matadadu, maximalmatadadu)
    print("Menghitung Peluang Munculnya Minimal Mata Dadu dari setiap Dadu")
    print("Banyaknya Dadu yang dimiliki\t: ", banyakdadu)
    print("Banyaknya Mata Dadu yang dimiliki oleh setiap Dadunya\t: ", matadadu)
    print("Banyaknya Mata Dadu yang dicari pada setiap Dadu\t: ", maximalmatadadu)
    print("Peluang yang muncul adalah\t: ", Hasilpeluang, "%")

    # Bola
    hijau = 2
    hitam = 2
    merah = 2
    carihijau = 2
    carihitam = 1
    carimerah = 1

    Hasilpeluang = Peluang.peluangBola(hijau, hitam, merah, carihijau, carihitam, carimerah)
    print("\nMenghitung Peluang Munculnya Bola diantara banyaknya Bola dengan Variasi Warna")
    print("Banyaknya Bola hijau yang dimiliki\t: ", hijau)
    print("Banyaknya Bola hitam yang dimiliki\t: ", hitam)
    print("Banyaknya Bola merah yang dimiliki\t: ", merah)
    print("Banyaknya Bola hijau yang akan dicari\t: ", carihijau)
    print("Banyaknya Bola hitam yang akan dicari\t: ", carihitam)
    print("Banyaknya Bola merah yang akan dicari\t: ", carimerah)
    print("Peluang yang muncul adalah\t: ", Hasilpeluang, "%")

    # Angka
    banyakangka = 100
    banyakangkacari = 25

    Hasilpeluang = Peluang.peluangAngka (banyakangka, banyakangkacari)
    print("\nMenghitung Peluang Munculnya Suatu Angka ")
    print("Banyaknya Angka yang dimiliki\t: ", banyakangka)
    print("Banyaknya Angka yang akan dicari\t: ", banyakangkacari)
    print("Peluang yang muncul adalah\t: ", Hasilpeluang, "%")


if __name__ == "__main__":
    main()
