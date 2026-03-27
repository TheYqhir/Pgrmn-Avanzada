
# Práctica 1 - Generador de Personajes RPG

## 📖 Descripción

Esta práctica contiene dos programas que generan personajes aleatorios para juegos de rol (RPG), desarrollados como parte del curso de Sistemas Operativos.

### Programas incluidos:

1. **generador_personaje.c** - Versión en lenguaje C
2. **generador_personaje.py** - Versión en lenguaje Python

Ambos programas generan aleatoriamente los 6 atributos clásicos de D&D:
- Fuerza
- Destreza
- Constitución
- Inteligencia
- Sabiduría
- Carisma


## 🚀 Instrucciones de uso

### Programa en C

**Compilar:**
```bash
gcc generador_personaje.c -o generador_personaje
```

**Ejecutar:**
```bash
./generador_personaje
```

En Windows:
```bash
generador_personaje.exe
```

### Programa en Python

**Ejecutar:**
```bash
python generador_personaje.py
```

O en sistemas Unix/Linux:
```bash
python3 generador_personaje.py
```

## 📋 Funcionalidades

- Solicita el nombre del personaje al usuario
- Genera valores aleatorios para cada atributo
- Muestra una hoja de personaje formateada
- Valida que se ingrese un nombre válido

### Diferencias entre versiones:

| Característica | C | Python |
|----------------|---|--------|
| Rango de atributos | 6-18 | 3-18 |
| Formato de salida | Alineado a la izquierda | Alineado a la izquierda |
| Entrada de texto | fgets() | input() |


**Última actualización:** 27 de marzo de 2026
