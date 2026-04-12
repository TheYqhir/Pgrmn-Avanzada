# Carpeta de Código Fuente (Source)

Esta carpeta contiene la lógica principal del sistema de adquisición de datos.

## Archivos
* **`run_acquisition.py`**: Script principal que gestiona la conexión serial, la captura de datos de sensores (Temperatura/LDR), la aplicación del filtro de media móvil y la generación de reportes.

## Instrucciones de Ejecución
Para ejecutar el script desde la raíz del proyecto, asegúrate de tener el entorno virtual activo y usa los siguientes comandos:

### Modo Simulación (Para pruebas rápidas sin hardware)
```bash
python F04/src/run_acquisition.py --mode sim
