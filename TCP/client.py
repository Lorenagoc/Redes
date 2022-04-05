'''
Aula prática 2 - Introdução à programação de Redes - Cefet/MG
Tema: Sockets
Referência: https://wiki.python.org.br/SocketBasico
'''

# Biblioteca para trabalhar com sockets
import socket

# Endereco IP do Servidor
HOST = '192.168.100.5'
# Porta do Servidor
PORT = 5000

# Diz ao sistema operacional que desejamos criar um socket
# AF_INET: Família endereços IPv4
# SOCK_STREAM: Protocolo TCP na camada de transporte
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Criação do socket TCP indicando a porta do servidor
dest = (HOST, PORT)

# Estabelecendo conexão
tcp.connect(dest)

print('Para sair use CTRL+X\n')
msg = input()

#Enquanto não for usado CTRL+X
while msg != '\x18':
    # Enviando mensagem
    tcp.send(msg.encode())

    # Recebe nova mensagem
    msg_upper = tcp.recv(1024)
    print("Recebi de volta = ",msg_upper.decode(),"\n")
    msg = input()
tcp.close()