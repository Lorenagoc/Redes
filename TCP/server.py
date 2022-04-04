'''
Aula prática 2 - Introdução à programação de Redes - Cefet/MG
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
# SOCK_STREAM: Protocolo TCP na camada de transporte
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Criação do socket TCP indicando a porta
orig = (HOST, PORT)

# Coloca endereço e porta no socket
tcp.bind(orig)

# Instrui o sistema operacional para colocar o socket em modo de ouvinte
tcp.listen(1)

while True:
    # Aceita nova conexão
    connection, client = tcp.accept()
    print('Conectando ao cliente = ', client)
    while True:
        # Recebe dados enquanto ainda houver
        msg = connection.recv(1024)
        if not msg: break
        print("Recebi = ",msg," do cliente ",client)
    print('Finalizando conexao do cliente', client)
    connection.close()