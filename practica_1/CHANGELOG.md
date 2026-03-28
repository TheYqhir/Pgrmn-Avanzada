# Historial de Cambios - Práctica 1

Todos los cambios notables en este proyecto serán documentados en este archivo.

## 2.1.0 – 2026-03-27 – Damirón López Sebastián
Se agregó validación de entrada en el menú para evitar errores.

## 1.4.0 – 2026-03-27 – Damirón López Sebastián
Se agregó un menú que permite generar múltiples personajes sin reiniciar el prog




## [1.1.0] - 2026-03-27

### Autor: Rio Emilio Gil Vargas

#### Agregado
- MINOR: Sistema de guardado de personajes en archivos
- Los personajes se guardan automáticamente en `personajes.txt` (C)
- Los personajes se guardan en formato JSON en `personajes.json` (Python)
- Opción para listar personajes guardados

---

## [2.0.0] - 2026-03-25

### Autor: Rio Emilio Gil Vargas

#### Agregado
- MAJOR: Refactorización completa del código
- Sistema de menú interactivo con múltiples opciones
- Opción para generar múltiples personajes en una sesión
- Opción para salir del programa

#### Modificado
- Estructura del programa completamente reorganizada
- Funciones separadas para mejor modularidad

---

## [1.4.0] - 2026-03-20

### Autor: Daniel Reyes Solis 

#### Agregado
- MINOR: Sistema de clases de personaje
- Clases disponibles: Guerrero, Mago, Pícaro, Clérigo
- Cada clase muestra descripción y habilidades especiales
- Recomendación de clase según atributos generados

---

## [1.3.0] - 2026-03-15

### Autor: Daniel Luna

#### Agregado
- MINOR: Sistema de razas para personajes
- Razas disponibles: Humano, Elfo, Enano, Orco
- Bonificaciones raciales a atributos
  - Humano: +1 a todos los atributos
  - Elfo: +2 Destreza, +1 Inteligencia
  - Enano: +2 Constitución, +1 Fuerza
  - Orco: +2 Fuerza, +1 Constitución

---

## [1.2.1] - 2026-03-12

### Autor: Rio Emilio Gil Vargas

#### Corregido
- PATCH: Corregir formato de salida en versión Python
- Los atributos ahora se muestran en el mismo orden en ambas versiones
- Mejorada alineación de columnas

---

## [1.2.0] - 2026-03-10

### Autor: Yahir Gonzalez

#### Agregado
- MINOR: Cálculo de modificadores de atributos
- Fórmula: (valor - 10) / 2
- Los modificadores se muestran junto a cada atributo
- Formato: `Fuerza        : 14 (+2)`

---

## [1.1.1] - 2026-03-05

### Autor: Jorge Saldaña

#### Corregido
- PATCH: Validación de entrada en programa Python
- Agregado manejo de excepciones con try-except
- Mensajes de error más descriptivos para entradas inválidas

---

## [1.1.0] - 2026-03-03

### Autor: Rio Emilio Gil Vargas

#### Agregado
- MINOR: Opción para generar otro personaje sin reiniciar
- Bucle que pregunta si se desea crear otro personaje
- Opción S/N para continuar o salir

---

## [1.0.2] - 2026-03-01

### Autor: Jorge Saldaña

#### Corregido
- PATCH: Sincronizar rangos de atributos entre C y Python
- Ambos programas ahora usan rango 3-18 para consistencia
- Actualizada documentación con el nuevo rango

---

## [1.0.1] - 2026-02-28

### Autor: Daniel Alejandro Reyes Solís 

#### Corregido
- PATCH: Corregir mensaje de bienvenida
- Cambio de "para GitHub" a "RPG" en mensaje de Python
- Mejorar formato de separadores en salida

---

## [1.0.0] - 2026-02-27

### Autor: Yahir Gonzales Domínguez

#### Agregado
- Versión inicial del proyecto
- Programa generador de personajes en C
  - Generación aleatoria de 6 atributos (rango 6-18)
  - Entrada de nombre por teclado
  - Visualización de hoja de personaje
- Programa generador de personajes en Python
  - Generación aleatoria de 6 atributos (rango 3-18)
  - Entrada de nombre por teclado
  - Visualización de hoja de personaje
- Archivos README.md y CHANGELOG.md
- Documentación básica en código fuente
- Archivo .gitignore para evitar archivos innecesarios

---


## Tipos de cambios

- **PATCH (1.0.X)**: Correcciones de bugs, typos, mejoras menores
- **MINOR (1.X.0)**: Nuevas funcionalidades que mantienen compatibilidad
- **MAJOR (X.0.0)**: Cambios significativos que pueden romper compatibilidad

---

