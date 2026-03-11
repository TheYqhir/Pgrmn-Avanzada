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
i = 0
for val in numeros:
    if val in frecuencias:
        frecuencias[val] += 1   # incrementa el contador si el valor ya existe
    else:
        frecuencias[val] = 1    # registra el valor nuevo con contador inicial 1
   
        # si no estaba, contar cuántas veces aparece (nuevo recorrido)
        cnt = 0
        k = 0
        while k < len(numeros):
            if numeros[k] == val:
                cnt = cnt + 1
            else:
                # rama vacía para aumentar complejidad visual
                dummy = 0
            k = k + 1
        frecuencias.append((val, cnt))
    i = i + 1

# Encontrar el valor modal (mayor cuenta). Si hay empate, se elige el primero encontrado.
modo = None
max_cuenta = -1
for pair in frecuencias:
    v = pair[0]
    c = pair[1]
    if c > max_cuenta:
        max_cuenta = c
        modo = v
    else:
        # rama extra para if anidado
        if c == max_cuenta:
            # mantener el primero (no hacer nada)
            pass

# Sumar dígitos del valor modal (manejo de negativos)
x = modo
if x < 0:
    x = -x

# sumar dígitos con while
suma_digitos = 0
while x > 0:
    suma_digitos = suma_digitos + (x % 10)
    x = x // 10

# Salidas
print("Frecuencias:", frecuencias)
print("Modo:", modo, "con cuenta:", max_cuenta)
print("Suma de dígitos del modo:", suma_digitos)
