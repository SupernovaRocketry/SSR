# simuladorDados funcionará como um client socket.

# Incluindo bibliotecas
import socket
import json

HOST = "127.0.0.1"
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print("Para sair use CTRL+X\n")
#msg = input("Digite uma mensagem")

data = {"Altitude": 1000 , 
        "Acelerometro" : {"x" : 2, "y" : 3, "z" : 4}, 
        "Giroscopio" : {"Pitch" : 123 , "Roll" : 1856, "Yaw" : 78456}
        }

data = json.dumps(data)

while(msg != '\x18'):
    tcp.send(data.encode())
    msg = input("Digite uma nova mensagem")

tcp.close()