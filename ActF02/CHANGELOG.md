

c_no_opt.c — v1.0.0 → v1.1.0

Autor: [Rio Emilio Gil Vargas]
Cambios:
Se agrega break al detectar el primer divisor, eliminando iteraciones inútiles.
Se limita la búsqueda de divisores a sqrt(m) en lugar de m-1, reduciendo la complejidad de O(n) a O(√n) por candidato.

python_no_opt.py — v1.0.0 → v1.1.0

Autor: [Rio Emilio Gil Vargas]
Se elimina el recorrido extra para contar ocurrencias de valores nuevos.
Se elimina la variable dummy del else vacío.
results/ — benchmarks agregados

Autor:  [Rio Emilio Gil Vargas]
Archivos añadidos:

results/benchmark_python.csv — 15 mediciones de la versión base y optimizada de Python (1 000 ejecuciones por muestra con timeit).
results/benchmark_c.csv — 15 mediciones de la versión base y optimizada de C (10 000 iteraciones internas por muestra con clock()).


Resultados: Python speedup ~5.69x, C speedup ~87x. Ver ANALYSIS.md para el análisis completo.



python_no_opt.py v1.0.0 -> v1.1.0.
Autor: (Daniel Alejandro Reyes Solis) 
cambios: Reducción de if/else a solo una operación. 

c_no_opt.c v1.0.0 -> v1.1.0.
Autor: (Daniel Alejandro Reyes Solis)
Cambios: Se optimiza la actualización de contadores usando operadores de incremento (++) y acumulación (+-) para mejorar claridad y eficiencia del codigo. 




python_no_opt.py — v1.0.0 → v1.1.0
Autor: (Damirón López Sebastian) 
cambios: 
una pequeña modificación cambiando los nombres de las variables para que fueran más claros y fáciles de entender.

La lógica del programa sigue siendo la misma: recorrer el diccionario frecuencias, comparar las repeticiones y actualizar la variable modo cuando se encuentra una frecuencia mayor.

Autor:[Rio Emilio Gil Vargas]
Cambios:
Se reemplaza la lista de tuplas con búsqueda lineal O(n²) por un diccionario O(n).
Se elimina el doble while anidado para construir frecuencias.


[1.0.0] - 2026-03-09
c_no_opt.c — versión base

Versión inicial con búsqueda de primos (sin break, sin límite de sqrt).

python_no_opt.py — versión base

Versión inicial con construcción de frecuencias O(n²) y bucles redundantes.
