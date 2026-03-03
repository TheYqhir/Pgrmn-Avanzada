import random

def generar_atributos():
    """Genera valores aleatorios para atributos de un personaje."""
    atributos = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]
    stats = {atrib: random.randint(3, 18) for atrib in atributos}
    return stats

def mostrar_personaje(nombre, stats):
    print(f"\n--- Hoja de Personaje: {nombre} ---")
    for k, v in stats.items():
        print(f"{k}: {v}")
    print("----------------------------------\n")

def main():
    print("¡Bienvenido al Generador de Personajes para GitHub!")
    nombre = input("Introduce el nombre de tu héroe: ")
    
    if nombre:
        mis_stats = generar_atributos()
        mostrar_personaje(nombre, mis_stats)
    else:
        print("Error: El personaje necesita un nombre para existir.")

if __name__ == "__main__":
    main()
