import platform
import psutil
import datetime
import sqlite3

# Obtener el sistema operativo actual
operating_system = platform.system()

if operating_system == 'Windows':
    print("Información del hardware en Windows:")
    print("-----------------------------------")
    print("CPU: ", platform.processor())
    print("RAM: ", round(psutil.virtual_memory().total / (1024**3), 2), "GB")
    print("Almacenamiento: ")
    for disk in psutil.disk_partitions():
        print(disk.device, "- Tamaño total:", round(psutil.disk_usage(disk.mountpoint).total / (1024**3), 2), "GB")
    print("-----------------------------------")

    # Guardar información en un archivo de texto
    file_name = "info_hardware_windows_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    with open(file_name, "w") as file:
        file.write("Información del hardware en Windows:\n")
        file.write("-----------------------------------\n")
        file.write("CPU: " + platform.processor() + "\n")
        file.write("RAM: " + str(round(psutil.virtual_memory().total / (1024**3), 2)) + " GB\n")
        file.write("Almacenamiento:\n")
        for disk in psutil.disk_partitions():
            file.write(disk.device + " - Tamaño total: " + str(round(psutil.disk_usage(disk.mountpoint).total / (1024**3), 2)) + " GB\n")
        file.write("-----------------------------------\n")

    # Guardar información en una base de datos
    conn = sqlite3.connect('info_hardware.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS info_windows
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 fecha TEXT,
                 cpu TEXT,
                 ram REAL,
                 almacenamiento TEXT)''')
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_info = platform.processor()
    ram_info = round(psutil.virtual_memory().total / (1024**3), 2)
    almacenamiento_info = ""
    for disk in psutil.disk_partitions():
        almacenamiento_info += disk.device + " - Tamaño total: " + str(round(psutil.disk_usage(disk.mountpoint).total / (1024**3), 2)) + " GB\n"
    c.execute("INSERT INTO info_windows (fecha, cpu, ram, almacenamiento) VALUES (?, ?, ?, ?)", (fecha_actual, cpu_info, ram_info, almacenamiento_info))
    conn.commit()
    conn.close()

elif operating_system == 'Linux':
    print("Información del hardware en Linux:")
    print("---------------------------------")
    print("CPU: ", platform.processor())
    print("RAM: ", round(psutil.virtual_memory().total / (1024**3), 2), "GB")
    print("Almacenamiento: ")
    for disk in psutil.disk_partitions():
        print(disk.device, "- Tamaño total:", round(psutil.disk_usage(disk.mountpoint).total / (1024**3), 2), "GB")
    print("---------------------------------")

    # Guardar información en un


