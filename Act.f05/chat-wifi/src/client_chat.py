"""
client_chat.py — Cliente TCP para chat punto a punto por Wi-Fi
Uso: python client_chat.py --host 192.168.x.x --port 5000
"""

import socket
import argparse
import threading
from utils import setup_logger, get_local_ip


def parse_args():
    parser = argparse.ArgumentParser(description="Cliente de chat TCP")
    parser.add_argument("--host", type=str, required=True,
                        help="IP del servidor al que conectarse")
    parser.add_argument("--port", type=int, default=5000,
                        help="Puerto TCP del servidor (default: 5000)")
    parser.add_argument("--log", type=str, default="results/logs/client.log",
                        help="Ruta del archivo de log")
    return parser.parse_args()


def main():
    args = parse_args()
    logger = setup_logger("client", args.log)

    local_ip = get_local_ip()
    print("=" * 50)
    print("  CLIENTE DE CHAT TCP")
    print("=" * 50)
    print(f"  Tu IP local: {local_ip}")
    print(f"  Servidor:    {args.host}:{args.port}")
    print(f"  Log:         {args.log}")
    print("=" * 50)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"\n[*] Conectando a {args.host}:{args.port}...")
        sock.connect((args.host, args.port))
        logger.info(f"Conectado al servidor {args.host}:{args.port}")
        print(f"[+] Conectado exitosamente.")
        print("    Escribe tu mensaje y presiona Enter. Escribe 'salir' para terminar.\n")
    except ConnectionRefusedError:
        print(f"[!] No se pudo conectar a {args.host}:{args.port}. ¿El servidor está corriendo?")
        logger.error(f"Conexión rechazada por {args.host}:{args.port}")
        return
    except Exception as e:
        print(f"[!] Error al conectar: {e}")
        logger.error(f"Error al conectar: {e}")
        return

    stop_event = threading.Event()

    def receive_loop():
        while not stop_event.is_set():
            try:
                data = sock.recv(4096)
                if not data:
                    print("\n[!] El servidor cerró la conexión.")
                    logger.info("Servidor desconectado.")
                    stop_event.set()
                    break
                msg = data.decode("utf-8").strip()
                if msg.upper() == "SALIR":
                    print("\n[!] El servidor envió SALIR. Cerrando sesión.")
                    logger.info("Servidor envió SALIR.")
                    stop_event.set()
                    break
                print(f"\n  [Servidor] {msg}")
                print("  [Tú] ", end="", flush=True)
            except OSError:
                break

    recv_thread = threading.Thread(target=receive_loop, daemon=True)
    recv_thread.start()

    while not stop_event.is_set():
        try:
            msg = input("  [Tú] ").strip()
            if not msg:
                continue
            sock.sendall((msg + "\n").encode("utf-8"))
            logger.info(f"Enviado al servidor: {msg}")
            if msg.lower() == "salir":
                stop_event.set()
                break
        except (EOFError, KeyboardInterrupt):
            print("\n[!] Interrumpido por el usuario.")
            stop_event.set()
            break

    sock.close()
    logger.info("Socket cliente cerrado.")
    print("\n[*] Desconectado. ¡Hasta luego!")


if __name__ == "__main__":
    main()

