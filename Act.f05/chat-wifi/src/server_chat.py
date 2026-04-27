import socket
import threading

HOST = '0.0.0.0'  # Escucha en todas las interfaces
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clientes = []

def manejar_cliente(conn, addr):
    print(f"[NUEVA CONEXIÓN] {addr} conectado.")
    while True:
        try:
            mensaje = conn.recv(1024).decode('utf-8')
            if not mensaje:
                break
            print(f"{addr}: {mensaje}")
            
            # Reenviar a todos los clientes
            for cliente in clientes:
                if cliente != conn:
                    cliente.send(mensaje.encode('utf-8'))
        except:
            break

    print(f"[DESCONECTADO] {addr}")
    clientes.remove(conn)
    conn.close()

print("[SERVIDOR LISTO] Esperando conexiones...")

while True:
    conn, addr = server.accept()
    clientes.append(conn)

    hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
    hilo.start()
