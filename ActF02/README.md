Optimización de Código — Python y C
Repositorio de la actividad de optimización de código para la materia. Contiene las versiones base y optimizadas de dos programas: uno en Python y uno en C, junto con resultados de benchmarks, análisis de mejoras y registro de cambios.
Descripción de los programas
c_no_opt.c
Itera los enteros desde 2 hasta N para encontrar números primos. Por cada primo encontrado actualiza un contador, acumula su valor y clasifica si es par o impar.

Versión actual: 1.1.0
Optimizaciones aplicadas: límite de divisores reducido a √N, break al detectar divisor, eliminación de ramas y variables redundantes.

python_no_opt.py
Recorre una lista de enteros, calcula la frecuencia de cada valor, determina el modo (valor más frecuente) y calcula la suma de dígitos de ese modo.

Versión actual: 1.1.0
Optimizaciones aplicadas: reemplazo de lista de tuplas O(n²) por diccionario O(n), eliminación de bucles anidados y recorridos extra.

Resultados de benchmarks
Los resultados de las mediciones se encuentran en la carpeta results/. Cada archivo CSV contiene los tiempos de ejecución de ≥10 repeticiones para la versión base y la versión optimizada.
Consulta ANALYSIS.md para el análisis comparativo completo.

Entrega
Actividad: Organizador gráfico 1 en eMinus.
Versiones entregadas: python_no_opt.py v1.1.0 — c_no_opt.c v1.1.0
