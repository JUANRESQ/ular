class BangunDatar :
    def segitiga(): # Method/function
        n = 1
        while(n == 1):
            print("Menghitung Luas Segitiga")
            alas = float(input("Masukan Alas\t: "))
            tinggi = float(input("Masukan Tinggi\t: "))
            luas = (alas * tinggi)/2
            print("Luas Segitiga adalah\t: ",luas, "cm")
            coba = input("Apakah Anda Ingin Menghitung Lagi [y/t]: ")
            if(coba == "t"):
                break
    def persegipanjang():
        n = 1
        while(n == 1):
            print("Menghitung Luas Persegi Panjang")
            panjang = float(input("Masukan Panjang\t: "))
            lebar = float(input("Masukan Lebar\t: "))
            luas = panjang * lebar
            print("Luas Segitiga adalah\t: ",luas, "cm")
            coba = input("Apakah Anda Ingin Menghitung Lagi [y/t]: ")
            if(coba == "t"):
                break
    def lingkaran() :
        n = 1
        while(n == 1):
            print("Menghitung Luas Lingkaran")
            r = float(input("Masukan jari-jari\t: "))
            luas = (22/7)*r*r
            print("Luas Segitiga adalah\t: ",luas, "cm")
            coba = input("Apakah Anda Ingin Menghitung Lagi [y/t]: ")
            if(coba == "t"):
                break
            
def menu_awal():
    while(True):
        print("="*35)
        print("Aplikasi Menghitung Bangun Ruang")
        print("="*35)
        print("Pilihan Rumus Bangun Ruang :")
        print("[1] Hitung Luas Segitiga")
        print("[2] Hitung Luas Persegi Panjang")
        print("[3] Hitung Luas Lingkaran")
        print("[4] Exit")
        print("="*35)
        pil = int(input("Masukan Pilihan Anda\t: "))
        if(pil == 1):
            BangunDatar.segitiga()
        elif (pil == 2):
            BangunDatar.persegipanjang()
        elif (pil == 3):
            BangunDatar.lingkaran()
        elif (pil == 4):
            print("Kamsahamida")
            exit()
        else :
            print("Masukan Pilihan Dengan Benar")
menu_awal()