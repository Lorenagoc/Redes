'''
Aula prática 2 - Introdução à programação de Redes - Cefet/MG
Integrantes: Bruna Gomes Camilo e Lorena Gomes de Oliveira Cabral
Tema: Sockets
Referência: https://wiki.python.org.br/SocketBasico
'''

# Biblioteca para trabalhar com sockets
import socket 

# Endereco IP do Servidor (vai funcionar para qualquer IP que a máquina tenha)
HOST = ''
# Porta do Servidor
PORT = 5000

# Diz ao sistema operacional que desejamos criar um socket
# AF_INET: Família endereços IPv4
# SOCK_DGRAM: Protocolo UDP na camada de transporte 
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Criação do socket UDP indicando a porta
orig = (HOST, PORT)

# Realiza a associação entre o socket e o endereço do servidor
udp.bind(orig)

# Loop infinito para executar o código no servidor
while True:
    # Recebe dados do socket
    msg, client = udp.recvfrom(1024)
    print("Recebi = ",msg.decode("utf8")," do cliente ", client)
    # Converte letras minúsculas em maiúsculas
    msg_upper = msg.upper()
    # Envia nova mensagem ao cliente
    udp.sendto(msg_upper, client)
udp.close()