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
    except ConnectionRefusedError:
        print("[-] Falha na conexão. Verifique se o servidor está em execução.")
        return

    # --- Parte Gráfica (agora dentro do 'try' para garantir que só execute se houver conexão) ---
    root = tk.Tk()
    root.title("Acesso Remoto")
    label = tk.Label(root)
    label.pack()

    # ==================================================================
    # === INÍCIO DAS CORREÇÕES (CLIENTE) ===============================
    # ==================================================================

    # CORREÇÃO 1: Funções movidas para dentro de 'iniciar_cliente' para terem acesso ao 'client_socket'
    def on_mouse_move(event):
        command = f"MOUSE_MOVE,{event.x},{event.y}"
        client_socket.send(command.encode())

    def on_mouse_click(event):
        command = f"MOUSE_CLICK,{event.num}"  # 1 para esquerdo, 3 para direito
        client_socket.send(command.encode())

    def on_key_press(event):
        command = f"KEY_PRESS,{event.keysym}"
        client_socket.send(command.encode())

    # CORREÇÃO 2: Adicionado o bind que faltava para o movimento do mouse
    label.bind("<Motion>", on_mouse_move)
    label.bind("<Button-1>", on_mouse_click)
    label.bind("<Button-3>", on_mouse_click)
    root.bind("<KeyPress>", on_key_press)

    # ==================================================================
    # === FIM DAS CORREÇÕES (CLIENTE) ==================================
    # ==================================================================

    payload_size = struct.calcsize(">L")
    data = b""

    while True:
        try:
            # Recebimento da imagem (lógica original está correta)
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
        
        except tk.TclError:
            # CORREÇÃO 3: Trata o erro que ocorre quando o usuário fecha a janela
            print("[-] Janela fechada, encerrando conexão.")
            break
        except Exception as e:
            print(f"[-] Erro: {e}")
            break

    client_socket.close()

if __name__ == '__main__':
    iniciar_cliente()