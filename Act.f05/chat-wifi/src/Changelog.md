# CHANGELOG

## [Etapa 1] - Implementación base del chat TCP

### R

* **feat:** creación del servidor TCP usando sockets (`socket.AF_INET`, `socket.SOCK_STREAM`).
* **feat:** configuración inicial de `HOST = '0.0.0.0'` y `PORT = 5000`.
* **feat:** implementación de `bind()` y `listen()` para habilitar recepción de conexiones.

---

### DANIEL ALEJANDRO REYES SOLIS

* **feat:** implementación de la función `manejar_cliente(conn, addr)` para gestionar cada cliente conectado.
* **feat:** uso de `recv()` y `decode('utf-8')` para recibir mensajes del cliente.
* **feat:** impresión de mensajes recibidos en consola con formato `addr: mensaje`.

---

### Y

* **feat:** implementación de lista global `clientes` para almacenar conexiones activas.
* **feat:** lógica de reenvío de mensajes a todos los clientes conectados excepto el emisor.
* **feat:** uso de `send()` para retransmitir mensajes en el chat.

---

### S

* **feat:** manejo básico de errores con bloque `try/except` en recepción de mensajes.
* **feat:** detección de desconexión cuando `recv()` retorna vacío.
* **feat:** eliminación de clientes desconectados de la lista `clientes`.

---

### C

* **feat:** implementación del cliente TCP con `socket()` y `connect()`.
* **feat:** configuración manual de la IP del servidor (`HOST = '192.168.0.102'`).
* **feat:** envío de mensajes desde consola usando `input()` y `send()`.

---

### M

* **feat:** implementación de recepción de mensajes en el cliente con `recv()` y `decode()`.
* **feat:** uso de `threading.Thread` para ejecución concurrente de envío y recepción.
* **feat:** manejo de error de conexión en cliente y cierre del socket.

---

## [Notas]

* El sistema permite comunicación básica tipo chat entre múltiples clientes.
* La transmisión se realiza en texto plano sin cifrado.
* No se implementa persistencia de mensajes ni autenticación de usuarios.

