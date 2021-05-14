# supervisorio funcionará como um servidor socket.

# Importando bibliotecas
import socket
import kivy
from kivy.app import App

HOST = ''                                                   # Define o ip com para esse programa. No caso, será utilizado o ip de feedback "127.0.0.1"
PORT = 5000                                                 # Define a porta de comunicação
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Cria o socket com o protocolo com o qual se deseja comunicar. No caso, TCP/IP
orig = (HOST, PORT)                                         # Lista contendo o ip e porta counicação
tcp.bind(orig)                                              # 
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print(f"Novo cliente conectado: {cliente}")
    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print(f'{cliente}, {msg}')
    print(f'Finalizada conexao do cliente {cliente}')
    con.close()

