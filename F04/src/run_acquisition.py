import os
import time
import json
import csv
import argparse
from datetime import datetime
import random
import sys
import numpy as np
import matplotlib.pyplot as plt

try:
    import serial
except ImportError:
    serial = None

def setup_environment():
    """Asegura que la carpeta results exista."""
    # Usamos ruta relativa simple para que funcione en GitHub y local
    if not os.path.exists('results'):
        os.makedirs('results')

def get_simulated_reading():
    """Genera datos simulados con algo de ruido."""
    temp = 25.0 + random.uniform(-1.5, 1.5)
    ldr = 500 + random.randint(-50, 50)
    return temp, ldr

def moving_average(data_list, window_size=5):
    """Aplica un filtro de media móvil simple."""
    if len(data_list) < window_size:
        return data_list[-1] if data_list else 0
    return sum(data_list[-window_size:]) / window_size

def main():
    setup_environment()

    parser = argparse.ArgumentParser(description="Adquisición de datos de sensores.")
    parser.add_argument('--mode', choices=['sim', 'serial'], default='sim', help="Modo de ejecución")
    parser.add_argument('--port', default='COM3', help="Puerto serial")
    parser.add_argument('--baud', type=int, default=115200, help="Baudrate")
    args = parser.parse_args()

    config = {
        'duration_seconds': 60,
        'sample_interval_s': 1.0,
        'serial_port': args.port,
        'baudrate': args.baud,
        'mode': args.mode,
        'filter_window': 5 
    }

    # Guardar Metadata
    with open('results/metadata.json', 'w') as f:
        json.dump(config, f, indent=4)

    # Guardar Entorno
    with open('results/environment.txt', 'w') as f:
        f.write(f"Python version: {sys.version}\n")
        f.write(f"Numpy version: {np.__version__}\n")

    ser = None
    if config['mode'] == 'serial':
        try:
            if serial is None:
                raise ImportError("Librería pyserial no instalada.")
            ser = serial.Serial(config['serial_port'], config['baudrate'], timeout=1)
            print(f"Conectado a {config['serial_port']}")
        except Exception as e:
            print(f"Error de conexión: {e}. Cambiando a simulación...")
            config['mode'] = 'sim'

    readings = [] 
    raw_temps = []
    raw_ldrs = []
    
    print("Iniciando adquisición por 60 segundos...")
    start_time = time.time()
    
    while time.time() - start_time < config['duration_seconds']:
        timestamp_iso = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        
        if config['mode'] == 'sim':
            temp_raw, ldr_raw = get_simulated_reading()
        else:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    parts = line.split(',')
                    temp_raw = float(parts[0])
                    ldr_raw = float(parts[1])
                else:
                    continue
            except:
                continue

        raw_temps.append(temp_raw)
        raw_ldrs.append(ldr_raw)

        temp_filtered = moving_average(raw_temps, config['filter_window'])
        ldr_filtered = moving_average(raw_ldrs, config['filter_window'])

        reading_tuple = (timestamp_iso, temp_raw, ldr_raw, temp_filtered, ldr_filtered)
        readings.append(reading_tuple)
        
        print(f"[{timestamp_iso}] Temp: {temp_raw:.2f} | LDR: {ldr_raw:.2f}")
        time.sleep(config['sample_interval_s'])

    if ser:
        ser.close()

    if not readings:
        print("No se adquirieron datos.")
        return

    # Guardar CSV
    final_csv = 'results/raw_readings.csv'
    with open(final_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'temp_raw', 'ldr_raw', 'temp_filtered', 'ldr_filtered'])
        for r in readings:
            writer.writerow(r)
    
    print(f"Datos guardados en {final_csv}")

    # Generar Gráfica
    timestamps = [datetime.strptime(r[0], '%Y-%m-%dT%H:%M:%SZ') for r in readings]
    temps_f = [r[3] for r in readings] 
    ldrs_f = [r[4] for r in readings]  

    fig, ax1 = plt.subplots(figsize=(10, 5))
    color = 'tab:red'
    ax1.set_xlabel('Tiempo')
    ax1.set_ylabel('Temperatura (°C)', color=color)
    ax1.plot(timestamps, temps_f, color=color, label='Temp (Filtrada)')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('LDR (ADC)', color=color)
    ax2.plot(timestamps, ldrs_f, color=color, label='LDR (Filtrada)')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Lecturas de Temperatura y LDR')
    plt.savefig('results/plot.png')
    print("Gráfica guardada en results/plot.png")

if __name__ == '__main__':
    main()
