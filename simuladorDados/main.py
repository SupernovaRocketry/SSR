# simuladorDados funcionará como um client socket.

# Incluindo bibliotecas
import socket

HOST = "127.0.0.1"
PORT = 500
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print("Para sair use CTRL+X\n")
msg = input("Digite uma mensagem")

while(msg != '\x18'):
    tcp.send(msg)
    msg = input("Digite uma nova mensagem")

tcp.close()