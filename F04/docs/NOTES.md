# Notas sobre cómo funciona el proyecto

## 1. Conexión con el sensor
Para que la computadora y el sensor (o el simulador) se entiendan, tienen que "hablar" a la misma velocidad.
* Usamos una velocidad de **115200**, que es bastante rápida para que no haya retrasos al recibir los datos.
* Si por algo se desconecta el cable, el programa espera un segundo antes de marcar error para no trabarse.

## 2. Sobre el Filtro (El suavizado)
Como los sensores a veces mandan datos con "saltos" raros, usamos el filtro de **Media Móvil**.
* **La ventana de 5:** Esto significa que el programa siempre saca el promedio de los últimos 5 datos recibidos. 
* ¿Por qué 5? Porque si promediamos muchos (por ejemplo, 50), el programa tardaría mucho en notar si la temperatura sube de verdad. Con 5 es rápido y estable.

## 3. ¿Cómo se guardan los datos?
El programa no guarda dato por dato en el archivo de Excel (CSV). Primero los junta todos en una lista dentro de la memoria y, ya que terminan los 60 segundos de prueba, escribe todo de un solo golpe. Esto hace que el programa sea más rápido y no gaste tanto disco duro.

## 4. Las gráficas
Usamos una herramienta que nos permite ver dos cosas al mismo tiempo en la misma imagen:
* La línea de **Temperatura** (en rojo).
* La línea de **Luz/LDR** (en azul).
Así es mucho más fácil ver si cuando hay más luz, también sube el calor.
