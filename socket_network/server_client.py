import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

socket_server.bind((host, port))
socket_server.listen(5)
print(f"[+] Listening on port: {port}")

while True:
    client_socket, addr = socket_server.accept()
    print(f"Dynamic port: {addr}")
    msg_fromclient = client_socket.recv(1024)
    print(f"[+] Data from client: {msg_fromclient.decode()}")
    client_socket.send(b"[+] Hello client")
    client_socket.close()
