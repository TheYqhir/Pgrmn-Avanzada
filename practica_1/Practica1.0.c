#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const char *atributos[] = {
    "Fuerza", "Destreza", "Constitución",
    "Inteligencia", "Sabiduría", "Carisma"
};

void generar_atributos(int stats[6]) {
    for (int i = 0; i < 6; i++) {
        stats[i] = (rand() % 13) + 6; // modifiqué el rango para que los atributos sean de 6 a 18, sebastian
    }
}

void mostrar_personaje(const char *nombre, int stats[6]) {
    printf("\n--- Hoja de Personaje: %s ---\n", nombre);
    for (int i = 0; i < 6; i++) {
        printf("%-14s: %d\n", atributos[i], stats[i]);
    }
    printf("----------------------------------\n\n");
}

int main() {
    srand(time(NULL));

    char nombre[50];
    printf("¡Bienvenido al Generador de Personajes!\n");
    printf("Introduce el nombre de tu heroe: ");
    fgets(nombre, sizeof(nombre), stdin);

    // Quitar salto de línea
    for (int i = 0; nombre[i]; i++) {
        if (nombre[i] == '\n') { nombre[i] = '\0'; break; }
    }

    if (nombre[0] != '\0') {
        int stats[6];
        generar_atributos(stats);
        mostrar_personaje(nombre, stats);
    } else {
        printf("Error: El personaje necesita un nombre para existir.\n");
    }

    return 0;
}
