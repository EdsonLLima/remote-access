import socket
import pickle
import struct
from PIL import ImageGrab

def iniciar_servidor():
    host = '0.0.0.0'  # Escuta em todas as interfaces de rede
    port = 9999

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[*] Escutando em {host}:{port}")

    conn, address = server_socket.accept()
    print(f"[+] Conexão de {address} estabelecida.")

    # Loop principal para manter a conexão
    while True:
        # Dentro do loop while True:
        try:
            # Captura a tela
            screenshot = ImageGrab.grab()
            screenshot_bytes = pickle.dumps(screenshot)

            # Envia o tamanho da imagem e a imagem
            size = len(screenshot_bytes)
            conn.sendall(struct.pack(">L", size) + screenshot_bytes)
            pass
        
        except ConnectionResetError:
            print("[-] Conexão perdida.")
            break

    conn.close()

if __name__ == '__main__':
    iniciar_servidor()