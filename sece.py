import requests
import pandas as pd
import json
import os

# Crear directorios si no existen
os.makedirs('data', exist_ok=True)

# Verificar si existe el archivo de configuración
if not os.path.exists('data/settings.json'):
    settings = {'session_id': ''}
    with open('data/settings.json', 'w') as f:
        json.dump(settings, f)

# Verificar si existe el archivo de campos
if not os.path.exists('data/campos.json'):
    campos = {'EF': ''}
    with open('data/campos.json', 'w') as f:
        json.dump(campos, f)

# Verificar si existe el archivo CSV
if not os.path.exists('data/alumnos.csv'):
    df = pd.DataFrame(columns=['ID_ALUMNO', 'CAMPO', 'TEXTO'])
    df.to_csv('data/alumnos.csv', index=False)

# Leer archivos
with open('data/settings.json', 'r') as f:
    settings = json.load(f)
with open('data/campos.json', 'r') as f:
    campos = json.load(f)
df = pd.read_csv('data/alumnos.csv')

# Iterar sobre cada fila en el CSV
for index, row in df.iterrows():
    id_alumno = row['ID_ALUMNO']
    campo = campos[row['CAMPO']]
    texto = row['TEXTO'].upper()

    # Preparar los parámetros
    params = {
        'parametros': f'{id_alumno}|DPS|{campo}|{texto}'
    }

    # Los headers de la petición
    headers = {
        'Cookie': f'PHPSESSID={settings["session_id"]}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'http://sece.guerrero.gob.mx:5000/evaluacion/campoformativo-listar-fila-frm.php'
    }

    print(f"Enviando petición para el alumno {id_alumno} en el campo {campo} con texto: {texto}...")
    response = requests.get(
        'http://sece.guerrero.gob.mx:5000/evaluacion/campoformativo-guardar-fila.php',
        params=params,
        headers=headers
    )

    # Muestra la respuesta
    print(f"Respuesta: {response.text}\n")