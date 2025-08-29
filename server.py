import socket

def start_server():
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 9999

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[*] Escutando em {host}:{port}")

    connection, address = server_socket.accept()
    print(f"[+] Conexão de {address} estabelecida.")

    # Main loop to maintain the connection
    while True:
        try:
            # Logic for receiving and sending data will go here
            pass
        except ConnectionResetError:
            print("[-] Conexão perdida.")
            break

    connection.close()

if __name__ == '__main__':
    start_server()