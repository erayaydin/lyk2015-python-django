import socket

# Socket bağlantısını oluştur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Adres bilgilerini belirle
server.bind(("127.0.0.1", 3000))
# Sunucuyu dinle
server.listen(1)


conn, addr = server.accept()
print("Bağlantı adresi:", addr)
while True:
    data = conn.recv(20)
    if not data: break
    print("Gelen veri:", data)
    conn.send(data)
conn.close()