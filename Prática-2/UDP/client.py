'''
Aula prática 2 - Introdução à programação de Redes - Cefet/MG
Integrantes: Bruna Gomes Camilo e Lorena Gomes de Oliveira Cabral
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
# SOCK_DGRAM: Protocolo UDP na camada de transporte 
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Criação do socket UDP indicando a porta do servidor
dest = (HOST, PORT)

print("Para sair use CTRL+X\n")

# Recebe dados do teclado
msg = input()

#Enquanto não for usado CTRL+X
while msg != '\x18':
    # Converte a mensagem para bytes e envia ao servidor
    udp.sendto(bytes(msg,"utf8"), dest)
    # Recebe nova mensagem do servidor
    msg_upper, server = udp.recvfrom(1024)
    print("Recebi de volta = ",msg_upper.decode("utf8")," do servidor ", server,"\n")
    msg = input()
udp.close()