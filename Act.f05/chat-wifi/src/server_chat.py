"""
server_chat.py — Servidor TCP para chat punto a punto por Wi-Fi
Uso: python server_chat.py --port 5000
"""

import socket
import argparse
import logging
import threading
from utils import setup_logger, get_local_ip

def parse_args():
    parser = argparse.ArgumentParser(description="Servidor de chat TCP")
    parser.add_argument("--host", type=str, default="0.0.0.0",
                        help="IP en la que escuchar (default: 0.0.0.0 = todas las interfaces)")
    parser.add_argument("--port", type=int, default=5000,
                        help="Puerto TCP (default: 5000)")
    parser.add_argument("--log", type=str, default="results/logs/server.log",
                        help="Ruta del archivo de log")
    return parser.parse_args()


def handle_client(conn, addr, logger):
    """Maneja la sesión de chat con un cliente conectado."""
    logger.info(f"Cliente conectado desde {addr}")
    print(f"\n[+] Cliente conectado: {addr[0]}:{addr[1]}")
    print("    Escribe tu mensaje y presiona Enter. Escribe 'salir' para terminar.\n")

    def receive_loop():
        while True:
            try:
                data = conn.recv(4096)
                if not data:
                    print("\n[!] El cliente cerró la conexión.")
                    logger.info("Cliente desconectado.")
                    break
                msg = data.decode("utf-8").strip()
                if msg.upper() == "SALIR":
                    print("\n[!] El cliente envió SALIR. Cerrando sesión.")
                    logger.info("Cliente envió SALIR.")
                    break
                print(f"\n  [Cliente] {msg}")
                print("  [Tú] ", end="", flush=True)
            except ConnectionResetError:
                print("\n[!] Conexión perdida.")
                logger.warning("Conexión perdida inesperadamente.")
                break

    recv_thread = threading.Thread(target=receive_loop, daemon=True)
    recv_thread.start()

    while recv_thread.is_alive():
        try:
            msg = input("  [Tú] ").strip()
            if not msg:
                continue
            conn.sendall((msg + "\n").encode("utf-8"))
            logger.info(f"Enviado al cliente: {msg}")
            if msg.lower() == "salir":
                break
        except (EOFError, KeyboardInterrupt):
            print("\n[!] Interrumpido por el usuario.")
            break

    conn.close()
    logger.info(f"Sesión terminada con {addr}")
    print(f"[*] Sesión con {addr[0]} finalizada.")


def main():
    args = parse_args()
    logger = setup_logger("server", args.log)

    local_ip = get_local_ip()
    print("=" * 50)
    print("  SERVIDOR DE CHAT TCP")
    print("=" * 50)
    print(f"  IP local:  {local_ip}")
    print(f"  Puerto:    {args.port}")
    print(f"  Log:       {args.log}")
    print("=" * 50)

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((args.host, args.port))
    server_sock.listen(1)

    logger.info(f"Servidor iniciado en {args.host}:{args.port} (IP local: {local_ip})")
    print(f"\n[*] Esperando conexión en el puerto {args.port}...")
    print("    (Comparte tu IP con el cliente para que se conecte)\n")

    try:
        conn, addr = server_sock.accept()
        handle_client(conn, addr, logger)
    except KeyboardInterrupt:
        print("\n[!] Servidor detenido por el usuario.")
        logger.info("Servidor detenido por KeyboardInterrupt.")
    finally:
        server_sock.close()
        logger.info("Socket del servidor cerrado.")


if __name__ == "__main__":
    main()

