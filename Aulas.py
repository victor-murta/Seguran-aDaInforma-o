#AULA 1
#ping : verfifica a coneção entre o ICMP INTERNER CONTROL MESSAGE PROTOCOL e o dispositivo
import os

"""
#---testando pin---
ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
os.system(f'ping {ip_ou_host}')"""

"""try:
    with open('./host.txt') as file:
        dump = file.read()
        dump = dump.splitlines()
        print(dump)
        print('-'*10)
        for ip in dump:
            os.system(f'ping -n 2 {ip}')
except:
    print('Ocorreu um erro ao abrir o arquivo host.txt')"""

#AUKA 2: SOCKET

#TCP - transmission control protocol : confere se todos os dados estão sendo enviados seguramente e rede.

# --- Cliente TCP ---
"""import socket
import sys 

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        print('Socket criado com sucesso')

    except socket.error as e:
        print(f'Houve um erro :{e}')
        sys.exit()
    
    HostAlvo = input('Digite o Host ou IP a ser conectado: ')
    PortaAlvo = int(input('Digite a porta a ser conctada: '))

    try:
        s.connect((HostAlvo, PortaAlvo))
        print(f'Cliente TCP criado com sucesso ...')
        print(f'''
        Host: {HostAlvo} 
        Porta: {PortaAlvo}
        ''')
        s.shutdown(2)
    except socket.error as e:
        print(f'Houve um erro, {e} no host {HostAlvo} na porta {PortaAlvo}')
        sys.exit()

if __name__ == "__main__":
    main()
"""



#UDP - user datagram protocol : envia um 'arquivo' ,datagrama, porém não tem garantias que cheguem fielmente. Uma conversa entre cliente e servidor

# import socket



# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# print(f'Clinete Socket: {s}')

# host = 'localhost'
# porta = 5433

# mensagemServidor = 'Opa,Servidor chamando para TERRA, servidor funcionando...'

# try:
#     print(f'Cliente enviou: {mensagemServidor}')
#     s.sendto(mensagemServidor.encode(),(host, 5432))

#     dados, servidor = s.recvfrom(4096)
#     dados = dados.decode()

#     print(f'Cliente: {dados}')
# finally:
#     print(f'Cliente fechando a conexão')
#     s.close()
    

#AULA 3 - Hash e Multithreading
#  
# import random
# import string

"""import random, string

tamanho = int(input('Digite o tamanho da senha: '))
#string.ascii_letters aceita letras em UPPERCASE e em lowercase
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+_,.;:/?'

rnd = random.SystemRandom()
r = ''.join(rnd.choice(chars) for i in range(tamanho))
print(r)
print(f'Tamanho da senha: {len(r)}')"""



'''import hashlib

arquivo1 = 'Senhas_Aula3/senha1.txt'
arquivo2 = 'Senhas_Aula3/senha2.txt'

hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'A senha do arquivo {arquivo1} é DIFERENTE da do arquivo {arquivo2}')
    print(f'Hash do arquivo: {hash1.hexdigest()}')
else:
    print(f'A senha do arquivo {arquivo1} é IGUAL da do arquivo {arquivo2}')
'''

# from threading import Thread
# from time import sleep

# def carro(velocidade, piloto):
#     trajeto = 0
#     while trajeto <= 100:
#         print(f'Piloto: {piloto} - Trajeto: {trajeto}')
#         trajeto += velocidade
#         sleep(0.5)


# t_carro1 = Thread(target = carro, args = [10, 'Python'])
# t_carro2 = Thread(target= carro, args = [20, 'Victor'])

# t_carro1.start()
# t_carro2.start()


# IP
'''import ipaddress

ip = '192.168.0.1'
rede = ipaddress.ip_network(ip)
endereço = ipaddress.ip_address(ip)

print(rede)
'''

#AULA 4 - desenvolendo um gerador de hashes 

'''
import hashlib

# resultado = hashlib.md5(b'Python Security')

def caso1(variavel):
    resultado = hashlib.md5(variavel.encode('utf-8'))
    resultado.hexdigest()
    return f'O hash da palavra {variavel.upper()} é {resultado.hexdigest()}'
    
def caso2(variavel):
    resultado = hashlib.sha1(variavel.encode('utf-8'))
    resultado.hexdigest()
    return f'O hash da palavra {variavel.upper()} é {resultado.hexdigest()}'

def caso3(variavel):
    resultado = hashlib.sha256(variavel.encode('utf-8'))
    resultado.hexdigest()
    return f'O hash da palavra {variavel.upper()} é {resultado.hexdigest()}'

def caso4(variavel):
    resultado = hashlib.sha512(variavel.encode('utf-8'))
    return f'O hash da palavra {variavel.upper()} é {resultado.hexdigest()}'

string = input('Senha ser gerada o hash: ')

print('
    - md5
    - sha1
    - sha256
    - sha512
'')


dicio = {
    'md5': caso1(string),
    'sha1': caso2(string),
    'sha256': caso3(string),
    'sha512': caso4(string)
}

escolha = ''
while escolha not in dicio.keys():
    escolha = input('Escolha: ').lower().strip()
    
# resultado = hashlib.md5(string.encode('utf-8'))
print(dicio[escolha])'''


#aula 4 - desenvolvendo uma wordlist


'''import itertools

resultado = itertools.permutations('abcdef', 5)
for r in resultado:
    print(''.join(r))
'''

#aula 4 - web scraping

'''
beautifulSoup: faz a extração de dados em arquivos HTML e XML
request: pode fazer requisições http em Python
'''

# from bs4 import BeautifulSoup
# import requests

# site = requests.get("https://www.climatempo.com.br/").content
# soup = BeautifulSoup(site, 'html.parser')

# # print(soup.prettify())

# temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
# print(temperatura.string)
# print(temperatura.title)

#aula 4 - web crawler

'''import requests 
from bs4 import BeautifulSoup
import operator
from collections import Counter



def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:
        if word in word_count :
            word_count[word] +=  1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " %(key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%&*(){}[]^:;.,/<>+-*="

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)


def start(url):
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
'''


#Aula 5 - Verificador de telefone: de qual estado ou de quem pertence o número

'''import phonenumbers

from phonenumbers import geocoder

print('Exemplo: +551140028922')
phone = input('Digite o telefone: ')
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
'''

#Aula 5 - desenvolvendo um ocultador de arquivos 

'''import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('senha.txt', atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else: 
    print('Arquivo não ocultado')'''


#Aula 5 - desenvolvendo um verificador de IP externo

# import re, json
# from urllib.request import urlopen

# url = 'https://ipinfo.io/json'

# resposta = urlopen(url)
# dados = json.load(resposta)

# ip = dados['ip']
# org = dados['org']
# cid = dados['city']
# pais = dados['country']

# print('Detales do IP externo: ')
# print(f'''
#     IP: {ip}
#     Org: {org}
#     Cidade: {cid}
#     País: {pais}
# ''')


#Aula 5 - ferramenta gráfica para abrir o navegador

import webbrowser
from tkinter import *

root = Tk()

root.title('Ferramenta para abrir o browser')
root.geometry('300x200')

def google():
    webbrowser.open('https://www.google.com')

myGoogle = Button(root, text = 'Abrir o Google', command = google).pack(pady= 20)

root.mainloop()











