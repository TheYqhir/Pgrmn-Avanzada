# Análisis de la Mejora: ¿Por qué usamos un Filtro?

## 1. El Problema: El "Ruido"
Cuando leemos datos de sensores (como la temperatura o la luz), los valores nunca son perfectos. A veces suben o bajan de golpe por una interferencia eléctrica o un error de lectura. A esto le llamamos **ruido**. Si graficamos esos datos crudos, la línea se ve muy "serruchada" o temblorosa.

## 2. La Solución: Filtro de Media Móvil
Para arreglar esto, programé un filtro de **Media Móvil**. 

**¿Cómo funciona?**
En lugar de graficar solo la última lectura, el programa voltea a ver las últimas 5 lecturas, saca el promedio de ellas y eso es lo que grafica. 
- Si llega una lectura loca (muy alta o muy baja), el promedio de las otras 4 la "suaviza".



## 3. ¿Qué ganamos con esto?
1. **Líneas más suaves:** La gráfica es mucho más fácil de leer. Ya no parece un zigzag loco, sino una curva suave.
2. **Datos confiables:** Evitamos que el sistema tome decisiones basadas en una sola lectura errónea.
3. **Rapidez:** Es un cálculo matemático muy simple (una suma y una división), por lo que el procesador no se esfuerza casi nada.

## 4. Conclusión
El filtro de media móvil fue un éxito. Ahora los datos de Temperatura y LDR son estables y profesionales, listos para ser usados en la siguiente etapa del proyecto.
