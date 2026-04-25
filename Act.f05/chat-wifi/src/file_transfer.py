""
file_transfer.py — Transferencia de archivos sobre TCP (mejora opcional)

Protocolo:
  1. Cliente envía encabezado:  FILENAME|SIZE|SHA256\n
  2. Servidor responde:         READY\n   (o ERR: motivo\n)
  3. Cliente envía contenido en bloques de CHUNK_SIZE bytes.
  4. Servidor calcula SHA256 del archivo recibido y responde:
       OK\n          — si el checksum coincide
       ERR:checksum\n — si no coincide

Uso como servidor (receptor):
    python file_transfer.py --mode server --port 5001

Uso como cliente (emisor):
    python file_transfer.py --mode client --host 192.168.x.x --port 5001 --file ruta/al/archivo.txt
"""

import socket
import hashlib
import argparse
import logging
import os
from pathlib import Path
from utils import setup_logger, format_size

CHUNK_SIZE = 4096          # bytes por bloque de envío
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB límite
RECEIVED_DIR = Path("results/received")
MAX_RETRIES = 3


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sha256_of_file(path: Path) -> str:
    """Calcula el SHA256 de un archivo en disco."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_bytes(data: bytes) -> str:
    """Calcula el SHA256 de un bloque de bytes en memoria."""
    return hashlib.sha256(data).hexdigest()


def recv_line(sock: socket.socket) -> str:
    """Lee bytes del socket hasta encontrar '\\n' y retorna la línea decodificada."""
    buf = b""
    while True:
        byte = sock.recv(1)
        if not byte or byte == b"\n":
            break
        buf += byte
    return buf.decode("utf-8").strip()


# ---------------------------------------------------------------------------
# Servidor (receptor)
# ---------------------------------------------------------------------------

def run_server(host: str, port: int, logger: logging.Logger):
    RECEIVED_DIR.mkdir(parents=True, exist_ok=True)

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(1)

    print(f"[*] Servidor de archivos escuchando en {host}:{port}")
    logger.info(f"Servidor de archivos iniciado en {host}:{port}")

    try:
        conn, addr = server_sock.accept()
        logger.info(f"Conexión de {addr}")
        print(f"[+] Cliente conectado: {addr}")

        header = recv_line(conn)
        logger.info(f"Encabezado recibido: {header}")

        parts = header.split("|")
        if len(parts) != 3:
            conn.sendall(b"ERR:encabezado invalido\n")
            logger.error("Encabezado inválido.")
            conn.close()
            return

        filename, size_str, client_checksum = parts
        file_size = int(size_str)

        print(f"[*] Archivo: {filename}  |  Tamaño: {format_size(file_size)}  |  SHA256: {client_checksum[:16]}...")

        if file_size > MAX_FILE_SIZE:
            conn.sendall(b"ERR:archivo demasiado grande (max 10 MB)\n")
            logger.error(f"Archivo rechazado: {format_size(file_size)} > 10 MB")
            conn.close()
            return

        conn.sendall(b"READY\n")

        # Recibir contenido
        dest_path = RECEIVED_DIR / Path(filename).name
        received = 0
        all_data = bytearray()

        print(f"[*] Recibiendo en: {dest_path}")
        while received < file_size:
            chunk = conn.recv(min(CHUNK_SIZE, file_size - received))
            if not chunk:
                break
            all_data.extend(chunk)
            received += len(chunk)
            pct = received / file_size * 100
            print(f"\r    Progreso: {pct:.1f}% ({format_size(received)} / {format_size(file_size)})", end="", flush=True)

        print()  # salto de línea tras barra de progreso

        # Verificar checksum
        server_checksum = sha256_of_bytes(bytes(all_data))
        if server_checksum == client_checksum:
            with open(dest_path, "wb") as f:
                f.write(all_data)
            conn.sendall(b"OK\n")
            logger.info(f"Archivo guardado: {dest_path} | SHA256: {server_checksum} | Tamaño: {format_size(received)}")
            print(f"[+] Archivo recibido y verificado correctamente.")
            print(f"    Guardado en: {dest_path}")
        else:
            conn.sendall(b"ERR:checksum\n")
            logger.error(f"Checksum no coincide. Esperado: {client_checksum} | Recibido: {server_checksum}")
            print("[!] Error: el checksum no coincide. Archivo descartado.")

        conn.close()
    except KeyboardInterrupt:
        print("\n[!] Servidor detenido.")
    finally:
        server_sock.close()


# ---------------------------------------------------------------------------
# Cliente (emisor)
# ---------------------------------------------------------------------------

def run_client(host: str, port: int, file_path: str, logger: logging.Logger):
    path = Path(file_path)
    if not path.exists():
        print(f"[!] El archivo '{file_path}' no existe.")
        logger.error(f"Archivo no encontrado: {file_path}")
        return

    file_size = path.stat().st_size
    if file_size > MAX_FILE_SIZE:
        print(f"[!] El archivo supera el límite de 10 MB ({format_size(file_size)}).")
        logger.error(f"Archivo demasiado grande: {format_size(file_size)}")
        return

    checksum = sha256_of_file(path)
    print(f"[*] Preparando envío de: {path.name}")
    print(f"    Tamaño:  {format_size(file_size)}")
    print(f"    SHA256:  {checksum[:32]}...")

    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n[*] Intento {attempt}/{MAX_RETRIES} — conectando a {host}:{port}...")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            logger.info(f"Conectado a {host}:{port} para enviar {path.name}")

            # Enviar encabezado
            header = f"{path.name}|{file_size}|{checksum}\n"
            sock.sendall(header.encode("utf-8"))

            # Esperar READY
            response = recv_line(sock)
            if response != "READY":
                print(f"[!] Servidor rechazó el archivo: {response}")
                logger.warning(f"Servidor respondió: {response}")
                sock.close()
                return

            # Enviar contenido
            sent = 0
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(CHUNK_SIZE), b""):
                    sock.sendall(chunk)
                    sent += len(chunk)
                    pct = sent / file_size * 100
                    print(f"\r    Progreso: {pct:.1f}% ({format_size(sent)} / {format_size(file_size)})", end="", flush=True)
            print()

            # Recibir confirmación
            result = recv_line(sock)
            if result == "OK":
                print(f"[+] ¡Archivo enviado y verificado correctamente!")
                logger.info(f"Transferencia exitosa: {path.name} | {format_size(file_size)} | SHA256: {checksum}")
                sock.close()
                return
            else:
                print(f"[!] Error del servidor: {result}. Reintentando...")
                logger.warning(f"Intento {attempt} fallido: {result}")
                sock.close()

        except ConnectionRefusedError:
            print(f"[!] No se pudo conectar a {host}:{port}.")
            logger.error(f"Intento {attempt}: conexión rechazada.")
        except Exception as e:
            print(f"[!] Error en intento {attempt}: {e}")
            logger.error(f"Intento {attempt} error: {e}")

    print(f"\n[!] Todos los intentos fallaron. Verifica la conexión.")
    logger.error("Transferencia fallida después de todos los reintentos.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Transferencia de archivos TCP")
    parser.add_argument("--mode", choices=["server", "client"], required=True,
                        help="Modo de ejecución: 'server' (receptor) o 'client' (emisor)")
    parser.add_argument("--host", type=str, default="0.0.0.0",
                        help="IP del servidor (para cliente: IP del servidor; para servidor: interfaz de escucha)")
    parser.add_argument("--port", type=int, default=5001,
                        help="Puerto TCP (default: 5001)")
    parser.add_argument("--file", type=str, default=None,
                        help="Ruta del archivo a enviar (solo en modo cliente)")
    parser.add_argument("--log", type=str, default="results/logs/file_transfer.log",
                        help="Ruta del archivo de log")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    logger = setup_logger("file_transfer", args.log)

    if args.mode == "server":
        run_server(args.host, args.port, logger)
    elif args.mode == "client":
        if not args.file:
            print("[!] Debes especificar --file en modo cliente.")
        else:
            run_client(args.host, args.port, args.file, logger)
