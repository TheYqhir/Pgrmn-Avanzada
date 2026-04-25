import socket
import threading

HOST = '192.168.0.102h'  
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

def recibir():
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            print("\nOtro:", mensaje)
        except:
            print("Error de conexión")
            cliente.close()
            break

def enviar():
    while True:
        mensaje = input()
        cliente.send(mensaje.encode('utf-8'))

threading.Thread(target=recibir).start()
threading.Thread(target=enviar).start()
