import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 3000))
client.send(5)
data = client.recv(1024)
client.close()

print("Gelen veri:", data)