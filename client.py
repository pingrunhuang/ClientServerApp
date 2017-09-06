#!/usr/bin/env python
from socket import *

def tcp_ipv4():
    HOST = '39.108.68.233'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    cs = socket(AF_INET, SOCK_STREAM)
    cs.connect(ADDR)

    while True:
        data = input('> ')
        cs.send(data.encode('utf-8'))
        data = cs.recv(BUFSIZ) 
        if not data:
            break
        print(data.decode('utf-8'))
    
    cs.close()

tcp_ipv4()    

def tcp_ipv6():
    HOST = '00:16:3e:08:df:07'
    PORT = 21567
    ADDR = (HOST, PORT)
    BUFSIZ = 1024
    
    sock = socket(AF_INET6, SOCK_STREAM)
    sock.connect(ADDR)
    
    while True:
        data = input('> ')
        if not data:
            break
        sock.send(data)
        response = sock.recv(BUFSIZ)
        if not response:
            break
        print(response.decode('utf-8'))
    sock.close()        
    

#def udp_ipv4():
    
