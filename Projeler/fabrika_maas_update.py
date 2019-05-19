print("""

<<<<<<<<<<<<<<< FABRİKA - İŞÇİ AYLIK MAAŞ HESAPLAMA >>>>>>>>>>>>>>>

İşçinin aylık çalıştığı toplam saate göre maaş hesaplama. Eğer işçi 350 veya daha fazla saat çalıştıysa maaşına zam yapılır.
""")
while True:
    print()
    saat=int(input("İşcinin Aylık Çalışma Saatini Giriniz -> "))
    if saat >= 350:
        print(saat * 12)

    elif saat >=215:
        print(saat*7)

    else:
        if (saat*7) < 2020:
            print(saat*7)
            print("Patronunuz çok az çalıştığınız için sizi KOVDU")
        else:
            print(saat*10)