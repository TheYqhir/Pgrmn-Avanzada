/*
 * Programa: Generador de Personajes RPG
 * Autor: Carlos Mendoza
 * Versión: 2.0.0
 * Descripción: Sistema completo con menú interactivo.
 * Fecha: 2026-03-25
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void limpiar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

const char *atributos[] = {
    "Fuerza", "Destreza", "Constitución",
    "Inteligencia", "Sabiduría", "Carisma"
};

int calcular_modificador(int valor) {
    return (valor - 10) / 2;
}

void generar_atributos(int stats[6]) {
    for (int i = 0; i < 6; i++) {
        stats[i] = (rand() % 16) + 3;
    }
}

void mostrar_personaje(const char *nombre, int stats[6]) {
    printf("\n--- Hoja de Personaje: %s ---\n", nombre);
    for (int i = 0; i < 6; i++) {
        int mod = calcular_modificador(stats[i]);
        printf("%-14s: %2d (%+d)\n", atributos[i], stats[i], mod);
    }
    printf("----------------------------------\n\n");
}

void crear_personaje() {
    char nombre[50];
    printf("\nIntroduce el nombre de tu héroe: ");
    getchar();
    fgets(nombre, sizeof(nombre), stdin);

    for (int i = 0; nombre[i]; i++) {
        if (nombre[i] == '\n') { 
            nombre[i] = '\0'; 
            break; 
        }
    }

    if (nombre[0] != '\0') {
        int stats[6];
        generar_atributos(stats);
        mostrar_personaje(nombre, stats);
    } else {
        printf("Error: El personaje necesita un nombre para existir.\n");
    }
}

void mostrar_menu() {
    printf("\n=== GENERADOR DE PERSONAJES RPG ===\n");
    printf("1. Crear nuevo personaje\n");
    printf("2. Acerca de\n");
    printf("3. Salir\n");
    printf("Selecciona una opción: ");
}

int main() {
    srand(time(NULL));
    int opcion;

    printf("¡Bienvenido al Generador de Personajes RPG!\n");

    do {
        mostrar_menu();
    if (scanf("%d", &opcion) != 1) {
    printf("\nEntrada inválida.\n");
    limpiar_buffer();
    opcion = 0;
    continue;
}

        switch(opcion) {
            case 1:
                crear_personaje();
                break;
            case 2:
                printf("\nGenerador de Personajes RPG v2.0.0\n");
                printf("Creado para práctica de Sistemas Operativos\n\n");
                break;
            case 3:
                printf("\n¡Hasta pronto, aventurero!\n");
                break;
            default:
                printf("\nOpción no válida. Intenta de nuevo.\n");
        }
    } while(opcion != 3);

    return 0;
}

   
