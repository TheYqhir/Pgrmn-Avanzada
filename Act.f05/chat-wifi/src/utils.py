"""
utils.py — Utilidades compartidas para servidor y cliente
"""

import logging
import socket
import os


def setup_logger(name: str, log_path: str) -> logging.Logger:
    """
    Configura y retorna un logger que escribe en archivo y en consola.

    Args:
        name:     Nombre del logger (ej. 'server', 'client').
        log_path: Ruta del archivo .log donde guardar los registros.

    Returns:
        logging.Logger configurado.
    """
    # Crear directorio de logs si no existe
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Evitar duplicar handlers si se llama varias veces
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Handler para archivo
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler para consola (solo WARNING y superior para no saturar)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_local_ip() -> str:
    """
    Obtiene la IP local de la máquina en la red activa.
    Usa un socket UDP temporal para determinar la IP de salida.

    Returns:
        Cadena con la IP local (ej. '192.168.1.10') o '127.0.0.1' si falla.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # No se envía nada; solo se usa para obtener la IP de la interfaz activa
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"


def format_size(size_bytes: int) -> str:
    """
    Formatea un tamaño en bytes a una cadena legible (KB, MB).

    Args:
        size_bytes: Tamaño en bytes.

    Returns:
        Cadena formateada, ej. '1.23 MB'.
    """
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes / 1024 ** 2:.2f} MB"
