#Integrantes: Vinicius Oliveira do Nascimento

import socket

def tcp_server():
  #configuração de ip e porta do servidor
  ip = '127.0.0.1'
  port = 8082

  #criação do servidor e processo de escuta da porta para 1 pessoa só
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((ip, port))
  server.listen(1)

  #recebendo a requisição do usuário e respondendo
  while True:
    client, address = server.accept()
    
    if not client:
      break

    print(f'servidor na porta: {address[1]}')

    string = client.recv(1024)
    string = string.decode('utf-8')
    string = string.upper()
    client.send(bytes(string, 'utf-8'))

    client.close()

def udp_server():
  ip = '127.0.0.2'
  port = '8083'
  bufferSize = 1024

  udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
  udp_server_socket.bind((ip, port))
  print(f'servidor na porta: {port}')

  while True:
    clients_requisition = udp_server_socket.recvfrom(bufferSize)
    
    if not clients_requisition[0]:
      break

    print(f'requisicao de: {clients_requisition[1]}')

    udp_server_socket.sendto(str.encode(clients_requisition[0].upper()), clients_requisition[1])

function_list = {
  '1': tcp_server,
  '2': udp_server,
}
server_type = input('1 -> tcp | 2 -> udp ')
selected_server = function_list[server_type]
selected_server()



