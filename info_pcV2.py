import platform
import subprocess

# Recopilamos la información del hardware utilizando el módulo platform
system_info = platform.uname()

# Obtenemos información adicional sobre el hardware utilizando el módulo subprocess
try:
    memoria_total = int(subprocess.check_output(['wmic', 'computersystem', 'get', 'TotalPhysicalMemory']).decode().split()[1]) // (1024**2)
except:
    memoria_total = 'No se pudo obtener información'

try:
    almacenamiento_total = int(subprocess.check_output(['wmic', 'diskdrive', 'get', 'Size']).decode().split()[1]) // (1024**3)
except:
    almacenamiento_total = 'No se pudo obtener información'

try:
    almacenamiento_disponible = int(subprocess.check_output(['wmic', 'logicaldisk', 'get', 'FreeSpace']).decode().split()[1]) // (1024**3)
except:
    almacenamiento_disponible = 'No se pudo obtener información'

# Creamos un archivo de texto para almacenar la información
with open('informacion_hardware.txt', 'w') as archivo:
    archivo.write('Información del hardware:\n\n')
    archivo.write(f'Sistema operativo:\t{system_info.system} {system_info.release}\n')
    archivo.write(f'Nombre del nodo:\t{system_info.node}\n')
    archivo.write(f'Procesador:\t\t{system_info.processor}\n')
    archivo.write(f'Arquitectura:\t\t{system_info.machine}\n')
    archivo.write(f'Memoria RAM total:\t{memoria_total} MB\n')
    archivo.write(f'Almacenamiento total:\t{almacenamiento_total} GB\n')
    archivo.write(f'Almacenamiento disponible:\t{almacenamiento_disponible} GB\n')
