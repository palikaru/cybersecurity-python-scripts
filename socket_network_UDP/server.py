import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 4444

server_socket.bind((host, port))
print(f"[+] Server listening on port: {port}")

data,addr = server_socket.recvfrom(1024)
print(addr)
print(f"Data from client: {data.decode()}")

server_socket.close()