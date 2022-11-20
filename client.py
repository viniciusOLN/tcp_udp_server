#Integrantes: Vinicius Oliveira do Nascimento

import socket

def tcp_operation():
  ip = '127.0.0.1'
  port = 8082

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.connect((ip, port))

  content = input('digite sua mensagem: ')
  server.send(bytes(content, 'utf-8'))

  response_server = server.recv(1024)
  response_server = response_server.decode('utf-8')

  print(f'server: {response_server}')

def udp_operation():
  server_address = ('127.0.0.2', 8083)
  buffer_size = 1024

  udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
  content = input('digite sua mensagem: ')

  udp_client_socket.sendto(str.encode(content), server_address)
  response_server = udp_client_socket.recvfrom(1024)

  print(f'server: {response_server[0]}')


function_list = {
  '1': tcp_operation,
  '2': udp_operation,
}

server_type = input('selecione uma opção: 1 -> tcp | 2 -> udp ')

while True:  
  
  if not server_type:
    break

  selected_option = function_list[server_type]
  selected_option()
