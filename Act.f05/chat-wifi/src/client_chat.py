"""
client_chat.py — Cliente TCP para chat punto a punto por Wi-Fi
Uso: python client_chat.py
     (edita HOST abajo con la IP del servidor)
"""

import socket
import threading
from utils import setup_logger, get_local_ip

HOST = '192.168.1.10'  # <-- cambia esto por la IP del servidor
PORT = 5000
LOG_PATH = "results/logs/client.log"

logger = setup_logger("client", LOG_PATH)


def recibir(sock):
    """Hilo que escucha mensajes del servidor continuamente."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[!] El servidor se desconectó.")
                logger.info("Servidor desconectado.")
                break
            msg = data.decode()
            print(f"\n[Servidor] {msg}")
            print("[Tú] ", end="", flush=True)
            logger.info(f"Recibido: {msg}")
        except:
            break


# --- Inicio del cliente ---
local_ip = get_local_ip()
print(f"Tu IP es: {local_ip}")
print(f"Conectando a {HOST}:{PORT}...\n")
logger.info(f"Intentando conectar a {HOST}:{PORT}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
except ConnectionRefusedError:
    print(f"[!] No se pudo conectar a {HOST}:{PORT}")
    print("    ¿Está corriendo el servidor?")
    logger.error("Conexión rechazada.")
    exit()

print(f"[+] Conectado al servidor {HOST}\n")
logger.info(f"Conectado a {HOST}:{PORT}")

# Lanzar hilo receptor
hilo = threading.Thread(target=recibir, args=(sock,), daemon=True)
hilo.start()

# Bucle principal: enviar mensajes
while True:
    try:
        msg = input("[Tú] ")
        if not msg:
            continue
        sock.sendall(msg.encode())
        logger.info(f"Enviado: {msg}")
        if msg.lower() == "salir":
            break
    except (KeyboardInterrupt, EOFError):
        break

sock.close()
logger.info("Cliente cerrado.")
print("Sesión terminada.")
