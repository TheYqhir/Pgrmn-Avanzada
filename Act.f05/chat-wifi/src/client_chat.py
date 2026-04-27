import socket
import threading

HOST = '192.168.0.102'  
PORT = 5000



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
