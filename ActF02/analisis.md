Metodología

Python: se usó timeit.repeat() con number=1000 y repeat=15 (1 000 ejecuciones por repetición, 15 muestras).
C: se midió con clock() internamente, promediando 10 000 iteraciones del algoritmo por muestra, con 15 muestras totales.
Ambas versiones (base v1.0.0 y optimizada v1.1.0) se ejecutaron en la misma máquina y condiciones.
Los resultados crudos están en results/benchmark_python.csv y results/benchmark_c.csv.


Resultados
Python
VersiónTiempo promedio (ms)base v1.0.09.67opt  v1.1.01.70Speedup5.69x
C
VersiónTiempo promedio (ms)base v1.0.01.107opt  v1.1.00.013Speedup87.37x

Análisis
Python — por qué mejoró ~5.7x
La versión base construía el diccionario de frecuencias con un doble while anidado: por cada elemento de la lista recorría toda la lista de frecuencias buscando si ya existía (O(n) por elemento), y si no lo encontraba, hacía un tercer recorrido completo para contar sus ocurrencias. Esto resultaba en una complejidad de O(n²) en el peor caso.
La versión optimizada usa un dict de Python, cuya operación de búsqueda e inserción es O(1) promedio gracias a su tabla hash interna. El recorrido completo se reduce a una sola pasada O(n). Además se eliminaron ramas else vacías y el bucle while de suma de dígitos se reemplazó por una comprensión de generador más eficiente.
C — por qué mejoró ~87x
La versión base probaba divisores desde d = 2 hasta d < m sin interrupción, incluso después de haber encontrado que m no era primo. Para m = 997 (primo) esto significa ~995 iteraciones del while. Multiplicado por los 999 candidatos del rango [2, 1000], el total de iteraciones es muy elevado.
La versión optimizada aplica dos mejoras combinadas:

Límite √m: si m tiene un divisor, uno de ellos es necesariamente ≤ √m. Esto reduce las iteraciones de O(m) a O(√m) por candidato.
break inmediato: al encontrar el primer divisor se sale del bucle, evitando seguir probando divisores innecesarios.

Para m = 1000, el límite baja de ~998 iteraciones a ~31. La combinación de ambas mejoras produce la ganancia de casi 90x observada.

Conclusión
ArchivoComplejidad baseComplejidad optSpeeduppython_no_opt.pyO(n²)O(n)~5.7xc_no_opt.cO(n × m)O(n × √m)~87x
Las optimizaciones no son solo de estilo: atacan directamente el número de operaciones que el procesador debe ejecutar, lo que se refleja en reducciones de tiempo medibles y consistentes.
