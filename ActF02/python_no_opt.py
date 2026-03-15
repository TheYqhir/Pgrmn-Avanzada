# python_no_opt.py
# Versión: 1.1.0
#Autor:
#Fecha: 2026/03/10
# Descripción:El programa calcula frecuencias de una lista de enteros,encuentra el modo y suma los dígitos del valor modal.
#Entrada: Lista de enteros "números".
#Salida: Frecuencias,modos,su cuenta y suma de dígitos de modo.
#MOD: v1.1.0- Se reemplaza lista de tuplas por diccionario, se elimina el doble while aninado y recorridos extra redundantes.

numeros = [3, -1, 0, 5, -7, 0, 2, 3, 3, -1, 5, 5, 5]  # lista de entrada

# Contadores y estructuras iniciales
frecuencias = {}  # diccionario {valor:cantidad_de_apariciones}
for val in numeros:
    if val in frecuencias:
        frecuencias[val] += 1   # incrementa el contador si el valor ya existe
    else:
        frecuencias[val] = 1    # registra el valor nuevo con contador inicial 1
 
# ── Búsqueda del modo ────────────────────────────────────────────────────────
 
modo = None
max_cuenta = -1
 
for v, c in frecuencias.items():
    if c > max_cuenta:   # actualiza el modo cuando se encuentra una frecuencia mayor
        max_cuenta = c
        modo = v
 
# ── Suma de dígitos del modo ─────────────────────────────────────────────────
 
x = abs(modo)                                  # valor absoluto para ignorar el signo
suma_digitos = sum(int(d) for d in str(x))     # convierte a string y suma cada dígito
 
# ── Salidas ──────────────────────────────────────────────────────────────────
 
print("Frecuencias:", list(frecuencias.items()))
print("Modo:", modo, "con cuenta:", max_cuenta)
print("Suma de dígitos del modo:", suma_digitos)
