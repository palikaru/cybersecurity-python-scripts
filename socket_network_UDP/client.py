import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_server = '127.0.0.1'
port = 4444

print(client_socket.sendto(b"[+] Hello server", (ip_server, port)))
client_socket.close()
