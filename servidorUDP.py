import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com SUCESSO')

host = 'localhost'
port = 5432
mensagem = '\nServidor: Olá cliente'

s.bind((host, port))


while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem ...')
        s.sendto(dados + (mensagem.encode()) , end)


