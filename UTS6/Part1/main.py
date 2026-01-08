import os
from utils import konversi_nilai_ke_label, konversi_label_ke_bobot


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_menu():
    print("===== MENU =====")
    print("1. Konversi Nilai ke Label")
    print("2. Konversi Label ke Bobot")
    print("3. Hitung Total SKS")
    print("4. Hitung Total Nilai")
    print("5. Hitung IPS")
    print("6. Keluar")


def input_pilihan():
    return input("Pilih Menu [1-6]: ")


def pause():
    input("\nTekan ENTER untuk lanjut...")


def menu_1():
    nilai = float(input("Nilai Mahasiswa : "))
    print("Label :", konversi_nilai_ke_label(nilai))


def menu_2():
    label = input("Label Nilai Mahasiswa : ")
    print("Bobot :", konversi_label_ke_bobot(label))


def menu_3():
    jumlah_data = int(input("Jumlah Data : "))
    total_sks = 0
    for i in range(1, jumlah_data + 1):
        total_sks += int(input(f"SKS {i}: "))
    print("Total SKS :", total_sks)


def menu_4():
    jumlah_data = int(input("Jumlah Data: "))

    list_sks = []
    list_nilai = []

    print("\n===== Input SKS =====")
    for i in range(jumlah_data):
        sks = int(input(f"SKS {i+1}: "))
        list_sks.append(sks)

    print("\n===== Input Nilai Mahasiswa =====")
    for i in range(jumlah_data):
        nilai = float(input(f"Nilai {i+1}: "))
        list_nilai.append(nilai)

    total_nilai = 0
    for i in range(jumlah_data):
        label = konversi_nilai_ke_label(list_nilai[i])
        bobot = konversi_label_ke_bobot(label)
        total_nilai += bobot * list_sks[i]

    print("\nTotal Nilai :", total_nilai)


def menu_5():
    jumlah_data = int(input("Jumlah Data: "))

    list_sks = []
    list_nilai = []

    print("\n===== Input SKS =====")
    for i in range(jumlah_data):
        list_sks.append(int(input(f"SKS {i+1}: ")))

    print("\n===== Input Nilai Mahasiswa =====")
    for i in range(jumlah_data):
        list_nilai.append(float(input(f"Nilai {i+1}: ")))

    total_sks = sum(list_sks)
    total_nilai = 0

    for i in range(jumlah_data):
        label = konversi_nilai_ke_label(list_nilai[i])
        bobot = konversi_label_ke_bobot(label)
        total_nilai += bobot * list_sks[i]

    if total_sks == 0:
        print("\nIPS : 0")
    else:
        ips = total_nilai / total_sks
        print("\nIPS :", round(ips, 2))


def jalankan_program():
    clear_screen()
    tampilkan_menu()

    while True:
        pilihan = input_pilihan()

        if pilihan == "1":
            menu_1()
        elif pilihan == "2":
            menu_2()
        elif pilihan == "3":
            menu_3()
        elif pilihan == "4":
            menu_4()
        elif pilihan == "5":
            menu_5()
        elif pilihan == "6":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")

        pause()
        clear_screen()
        tampilkan_menu()
