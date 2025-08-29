import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 4444

socket_server.bind((host, port))
print(f"[+] Server listening at port: {port}")
socket_server.listen(4)
client_socket, addr = socket_server.accept()

data_client = client_socket.recv(1024)
print(f"[+] Data from CLIENT: {data_client.decode()}")

client_socket.send(b"Hello client!")
client_socket.close()

