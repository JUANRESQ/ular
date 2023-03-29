import getpass

class Atm:
    def pilih_menu():
        print("="*48)
        print("\t\tATM BERSAMA")
        print("\tJl.S Parman No.14 Balikpapan Tengah")
        print("\t\tTelp.0542-48215")
        print("================ MENU PILIHAN =================")
        print("[1] Informasi Saldo")
        print("[2] Bayar")
        print("[3] Transfer")
        print("[4] Ambil Uang")
        print("[5] Keluar")
        print("="*45)
        pilih = int(input("Masukan Pilihan Menu [1/2/3/4/5]"))
        if(pilih == 1):
            n = 1
            while(n == 1):
                print("Menu: INFORMASI SALDO")
                print("Informasi Rekening Tabungan")
                print("Informasi Giro")
                kembali = input("Masukan Transaksi Lagi [Y/T]: ")
                if((kembali == "t") or (kembali == "T")):
                    Atm.pilih_menu()
                    continue
        elif(pilih == 2):
            n = 1
            while(n == 1):
                print("Menu: BAYAR")
                print("[1] BPJS\t[3] PDAM")
                print("[2] PLN\t[4] PULSA PASCA BAYAR")
                kembali = input("Masukan Transaksi Lagi [Y/T]: ")
                if((kembali == "t") or (kembali == "T")):
                    Atm.pilih_menu()
                    continue
        elif(pilih == 3):
            n = 1
            while(n == 1):
                print("Menu: TRANSFER")
                print("[1] Transfer Antar Bank")
                print("[2] Transfer Sesama Bank")
                kembali = input("Masukan Transaksi Lagi [Y/T]: ")
                if((kembali == "t") or (kembali == "T")):
                    Atm.pilih_menu()
                    continue
        elif(pilih == 4):
            saldo = 300000
            n = 1
            while(n == 1):
                print("Menu: AMBIL UANG")
                print("[1] Rp. 1.000.000,-")
                print("[2] Rp. 500.000,-")
                print("[3] Rp. 300.000,-")
                print("[4] Nominal Lain")
                print("="*45)
                uang1 = 1000000
                uang2 = 500000
                uang3 = 300000
                ambil = input("Masukan nilai uang yang akan diambil [1/2/3/4] ")
                if(ambil == 1):
                    saldo = saldo - uang1
                elif(ambil == 2):
                    saldo = saldo - uang2
                elif(ambil == 3):
                    saldo = saldo - uang3
                elif(ambil == 4):
                    uanglain = float(input("Masukan nominal uang yang diambil: Rp. "))
                    saldo = saldo - uanglain
                else :
                    print("Maaf Saldo Anda Tidak Cukup")
                    kembali = input("Masukan Transaksi Lagi [Y/T]: ")
                    if((kembali == "t") or (kembali == "T")):
                        Atm.pilih_menu()
                        continue
        elif(pilih == 5):
            print("Terimakasih silahkan ambil kartu anda")
            exit()
def menu_utama():
    pin = "12345"
    print("="*48)
    print("\t\tATM BERSAMA")
    print("\tJl.S Parman No.14 Balikpapan Tengah")
    print("\t\tTelp.0542-48215")
    print("================ MENU PILIHAN =================")
    for i in range(3) :
        sandi = getpass.getpass("Masukan PIN anda\t: ")
        if (sandi == pin):
            Atm.pilih_menu()
        else :
            print('PIN anda salah!')
            if i == 2 :
                print("Anda telah melakukan 3x percobaan")
                print("Kartu ATM terblokir")
                exit()
menu_utama()
    