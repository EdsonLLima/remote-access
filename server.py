import socket
import pickle
import struct
from PIL import ImageGrab
import pyautogui  # <--- CORREÇÃO 1: Import que estava faltando

def iniciar_servidor():
    host = '0.0.0.0'
    port = 9999

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"[*] Escutando em {host}:{port}")

    conn, address = server_socket.accept()
    print(f"[+] Conexão de {address} estabelecida.")

    while True:
        try:
            # Envio da imagem (lógica original está correta)
            screenshot = ImageGrab.grab()
            screenshot_bytes = pickle.dumps(screenshot)
            size = len(screenshot_bytes)
            conn.sendall(struct.pack(">L", size) + screenshot_bytes)

            # ==================================================================
            # === INÍCIO DA CORREÇÃO CRÍTICA (SERVIDOR) ========================
            # ==================================================================

            # CORREÇÃO 2: Implementado timeout para evitar o bloqueio (deadlock)
            conn.settimeout(0.01)  # Define um tempo de espera muito curto

            try:
                command_data = conn.recv(1024).decode()
                if command_data:
                    parts = command_data.split(',')
                    command_type = parts[0]

                    if command_type == "MOUSE_MOVE":
                        x, y = int(parts[1]), int(parts[2])
                        pyautogui.moveTo(x, y)
                    elif command_type == "MOUSE_CLICK":
                        button = int(parts[1])
                        if button == 1:
                            pyautogui.click()
                        elif button == 3:
                            pyautogui.rightClick()
                    elif command_type == "KEY_PRESS":
                        key = parts[1]
                        pyautogui.press(key)
            except socket.timeout:
                # Se nenhum comando chegar no tempo definido, o programa não trava e apenas continua
                pass
            
            conn.setblocking(True) # Restaura o comportamento padrão para o envio da imagem

            # ==================================================================
            # === FIM DA CORREÇÃO CRÍTICA (SERVIDOR) ===========================
            # ==================================================================

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            print("[-] Conexão perdida.")
            break

    conn.close()

if __name__ == '__main__':
    iniciar_servidor()