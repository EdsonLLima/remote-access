import socket
import pickle
import struct
import tkinter as tk
from PIL import Image, ImageTk

def iniciar_cliente():
    host = 'IP_DO_COMPUTADOR_X'  # Insira o IP do computador a ser acessado
    port = 9999

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
        print("[+] Conectado ao servidor.")
        # Após a conexão bem-sucedida
        root = tk.Tk()
        root.title("Acesso Remoto")
        label = tk.Label(root)
        label.pack()

        payload_size = struct.calcsize(">L")
        data = b""
        
    except ConnectionRefusedError:
        print("[-] Falha na conexão. Verifique se o servidor está em execução.")
        return

    # Loop principal para manter a conexão
    while True:
        # Dentro do loop while True:
        while len(data) < payload_size:
            data += client_socket.recv(4096)

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack(">L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        img = ImageTk.PhotoImage(image=Image.frombytes(frame.mode, frame.size, frame.tobytes()))
        label.config(image=img)
        label.image = img
        root.update()
        pass

    client_socket.close()

if __name__ == '__main__':
    iniciar_cliente()