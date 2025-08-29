import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_server = '127.0.0.1'
port = 9999

print(f"[+] Client conncetion at: {ip_server}:{port}")
client_socket.connect((ip_server, port))
print(f"[+] Connceted")

client_socket.send(b"[+] Hello server!")
msg_fromserver = client_socket.recv(1024)
print(f"Data from server: {msg_fromserver.decode()}")
client_socket.close()