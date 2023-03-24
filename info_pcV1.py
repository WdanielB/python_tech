import psutil
import platform
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Obtener información del sistema
cpu = psutil.cpu_brand()
os = platform.system() + " " + platform.release()

# Conectarse a Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google-creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Mi Hoja de Cálculo').sheet1

# Agregar información a la hoja de cálculo
row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), cpu, os]
sheet.append_row(row)

# Guardar información en un archivo de texto
filename = datetime.now().strftime('%Y-%m-%d') + " " + cpu + " " + os + ".txt"
with open(filename, 'w') as f:
    f.write("Procesador: " + cpu + "\n")
    f.write("Sistema operativo: " + os + "\n")
