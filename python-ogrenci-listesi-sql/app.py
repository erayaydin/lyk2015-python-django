import sqlite3

conn = sqlite3.connect("datatable.db")

status = True
kullanicilar = []
while status:
	print("Sıralamak için [S], Eklemek için [E] yazın, Çıkmak için [Q]")
	action = input("İşlem: ")
	action = action.lower()
	if(action == "s"):
		for kullanici in conn.execute("SELECT name,surname,age,work FROM OGRENCILER"):
			print("------")
			print("Ad:", kullanici[0])
			print("Soyad:", kullanici[1])
			print("Yaş:", kullanici[2])
			print("İş:", kullanici[3])
			print("------")
	elif(action == "e"):
		name = input("Ad:")
		surname = input("Soyad:")
		age = input("Yaş:")
		work = input("İş:")
		conn.execute("INSERT INTO OGRENCILER (ID,NAME,SURNAME,AGE,WORK) VALUES(NULL,'"+name+"','"+surname+"', '"+age+"', '"+work+"')")
	elif(action == "q"):
		print("Program sonlandırılıyor!")
		status = False

conn.close()
