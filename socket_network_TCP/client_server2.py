import socket

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_server = '127.0.0.1'
port = 9999

print(f"[+] Client connection at: {ip_server}:{port}")
client_server.connect((ip_server, port))
print(f"[+] Connected")

i = 0
while i < 5:
    msg_to_server = b"[+] Message from client2: Hello server!"
    client_server.send(msg_to_server)
    i = i + 1
    
msg = client_server.recv(1024)
print(f"[+] Data from server: {msg.decode()}")
client_server.close()