print("""

<<<<<<<<<<<<<<<< KULLANICI GİRİŞİ >>>>>>>>>>>>>>>

""")
username=input("Kullanıcı Adı: ")
password=input("Parola: ")

if len(password) >= len("12345678"):
	print("Sisteme Başarılı Bir Şekilde Giriş Yaptınız")
else: 
	while len(password) >= len("12345678"):
		print("Lütfen sekiz veya daha fazla karakterli bir parola girin")
		input=("Parola: ")

	
	print("Başarılı Bir Şekilde Sisteme Giriş Yaptınız")