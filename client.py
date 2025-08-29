import socket

def start_client():
    host = 'IP_DO_COMPUTADOR_X'  # Enter the IP of the computer to be accessed
    port = 9999

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print("[+] Conectado ao servidor.")
    except ConnectionRefusedError:
        print("[-] Falha na conexão. Verifique se o servidor está em execução.")
        return

    # Main loop to maintain the connection
    while True:
        # Logic for sending and receiving data will go here
        pass

    client_socket.close()

if __name__ == '__main__':
    start_client()