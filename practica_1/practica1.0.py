"""
Programa: Generador de Personajes RPG
Autor: Miguel Torres
Versión: 1.3.0
Descripción: Generador con sistema de razas y bonificaciones.
Fecha: 2026-03-15
"""

import random

RAZAS = {
    "Humano": {"Fuerza": 1, "Destreza": 1, "Constitución": 1, 
               "Inteligencia": 1, "Sabiduría": 1, "Carisma": 1},
    "Elfo": {"Destreza": 2, "Inteligencia": 1},
    "Enano": {"Constitución": 2, "Fuerza": 1},
    "Orco": {"Fuerza": 2, "Constitución": 1}
}

def calcular_modificador(valor):
    return (valor - 10) // 2

def generar_atributos():
    atributos = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]
    stats = {atrib: random.randint(3, 18) for atrib in atributos}
    return stats

def aplicar_raza(stats, raza):
    bonificaciones = RAZAS.get(raza, {})
    for atrib, bonus in bonificaciones.items():
        stats[atrib] = stats.get(atrib, 0) + bonus
    return stats

def mostrar_personaje(nombre, stats, raza):
    print(f"\n--- Hoja de Personaje: {nombre} ({raza}) ---")
    for k, v in stats.items():
        mod = calcular_modificador(v)
        print(f"{k:<14}: {v:2d} ({mod:+d})")
    print("----------------------------------\n")

def main():
    print("¡Bienvenido al Generador de Personajes RPG!")
    nombre = input("Introduce el nombre de tu héroe: ")
    
    if not nombre:
        print("Error: El personaje necesita un nombre para existir.")
        return
    
    print("\nRazas disponibles:")
    for i, raza in enumerate(RAZAS.keys(), 1):
        print(f"{i}. {raza}")
    
    try:
        opcion = int(input("Selecciona una raza (1-4): "))
        raza = list(RAZAS.keys())[opcion - 1]
    except (ValueError, IndexError):
        print("Opción inválida. Se usará Humano por defecto.")
        raza = "Humano"
    
    mis_stats = generar_atributos()
    mis_stats = aplicar_raza(mis_stats, raza)
    mostrar_personaje(nombre, mis_stats, raza)

if __name__ == "__main__":
    main()
