
print("=============================== Tahmin Oyunu =============================== ")
print("""

---------------------------------
  1 = Çok Kolay  =>  1 - 10
  2 = Kolay      =>  1 - 100
  3 = Orta       =>  1 - 1.000
  4 = Zor        =>  1 - 10.000
  5 = Çok Zor    =>  1 - 100.000
---------------------------------

""")
while True:
	seviye = int(input("Zorluk Seviyesi Seçiniz: "))

	if seviye == 1:

		import random

		sayi=random.randint(1,10)

		while True:
			print("==================")
			tahmin = int(input("Sayıyı Tahmin Edin: "))

			if tahmin == sayi:
				print("********************")
				print("  !!Doğru Tahmin!!")
				print("********************")
				break
			
			elif tahmin < sayi:
				print("==================")
				print("Daha Büyük")

			elif tahmin > sayi:
				print("==================")
				print("Daha Küçük")

	if seviye == 2:

		import random

		sayi=random.randint(1,100)

		while True:
			print("==================")
			tahmin = int(input("Sayıyı Tahmin Edin: "))

			if tahmin == sayi:
				print("********************")
				print("  !!Doğru Tahmin!!")
				print("********************")
				break

			elif tahmin < sayi:
				print("==================")
				print("Daha Büyük")

			elif tahmin > sayi:
				print("==================")
				print("Daha Küçük")
			
			
	if seviye == 3:

		import random

		sayi=random.randint(1,1000)

		while True:
			print("==================")
			tahmin = int(input("Sayıyı Tahmin Edin: "))

			if tahmin == sayi:
				print("********************")
				print("  !!Doğru Tahmin!!")
				print("********************")
				break

			elif tahmin < sayi:
				print("==================")
				print("Daha Büyük")

			elif tahmin > sayi:
				print("==================")
				print("Daha Küçük")
			
	if seviye == 4:

		import random

		sayi=random.randint(1,10000)

		while True:
			print("==================")
			tahmin = int(input("Sayıyı Tahmin Edin: "))

			if tahmin == sayi:
				print("********************")
				print("  !!Doğru Tahmin!!")
				print("********************")
				break

			elif tahmin < sayi:
				print("==================")
				print("Daha Büyük")

			elif tahmin > sayi:
				print("==================")
				print("Daha Küçük")
			
	if seviye == 5:

		import random

		sayi=random.randint(1,100000)
	
		while True:
			print("==================")
			tahmin = int(input("Sayıyı Tahmin Edin: "))

			if tahmin == sayi:
				print("********************")
				print("  !!Doğru Tahmin!!")
				print("********************")
				break

			elif tahmin < sayi:
				print("==================")
				print("Daha Büyük")

			elif tahmin > sayi:
				print("==================")
				print("Daha Küçük")
			
			

			

			