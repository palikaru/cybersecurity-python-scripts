import socket

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_server = '127.0.0.1'
port = 4444

msg_bytes = bytearray("-" *50, "UTF-8")

print(f"[+] Connection at: {ip_server}:{port}")
client_server.connect((ip_server, port))
print(f"[+] Connected!")

client_server.send(b"[+] Hello server from client_sever_bytes!")
bytes_fromserver = client_server.recv_into(msg_bytes)
print(bytes_fromserver)
client_server.close()


