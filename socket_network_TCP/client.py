import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_server = '127.0.0.1'
port_conn = 4444

print(f"[+] Client connection at: {ip_server}:{port_conn}")
client_socket.connect((ip_server, port_conn))
print(f"[+] Connected!")

client_socket.send(b"Hello sever!")
data_server = client_socket.recv(1024)
print(f"[+] Data from SERVER: {data_server.decode()}")
client_socket.close()
