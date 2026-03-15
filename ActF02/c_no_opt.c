/* c_no_opt.c
   Versión: 1.1.0
   El código en C itera los enteros desde 2 hasta N, para cada número prueba divisores 
   mediante un bucle while para determinar si es primo, marca el resultado con una variable
   booleana, y cuando detecta un primo actualiza el contador total, suma su valor a un acumulador 
   y clasifica si es par o impar; emplea for, while e if/else anidados para la generación de 
   candidatos, la verificación de divisores y la actualización de contadores y suma.
 MOD: v1.1.0 — se agrega break al detectar divisor, se limita búsqueda a sqrt(m),
                 se eliminan bloques redundantes (dummy, z) y se usan operadores ++ y +=.

*/


 
#include <stdio.h>
#include <stdlib.h>
#include <math.h>  /* para sqrt() */
 
int main() {
 
    int N = 1000;              /* límite superior del rango de búsqueda */
    int count_primos = 0;      /* cantidad de primos encontrados */
    long long suma_primos = 0; /* long long para evitar desbordamiento en sumas grandes */
    int primos_pares = 0;      /* solo el 2 caerá aquí */
    int primos_impares = 0;    /* todos los demás primos */
 
    for (int m = 2; m <= N; m++) {  /* recorre cada candidato desde 2 hasta N */
 
        int es_primo = 1;  /* bandera: asumimos primo hasta encontrar un divisor */
        int limite = (int)sqrt((double)m);  /* MOD: v1.1.0 — límite reducido de m-1 a sqrt(m) */
 
        int d = 2;  /* primer divisor candidato */
        while (d <= limite) {
            if (m % d == 0) {   /* si d divide a m exactamente, m no es primo */
                es_primo = 0;
                break;  /* MOD: v1.1.0 — evita seguir iterando al encontrar un divisor */
            }
            d++;
        }
 
        if (es_primo) {
            count_primos++;       /* contamos el primo */
            suma_primos += m;     /* acumulamos su valor */
            if (m % 2 == 0)
                primos_pares++;   /* primo par (únicamente m = 2) */
            else
                primos_impares++; /* primo impar */
        }
    }
 
    /* impresión de resultados */
    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);
 
    return 0;
}
