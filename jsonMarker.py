import os
import json

# Directorio donde se encuentran los archivos .py y .txt
directorio = 'ruta/a/la/carpeta'

# Obtener la lista de archivos .py en el directorio
archivos_py = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.py')]

# Crear una lista para almacenar los objetos del archivo JSON
objetos_json = []

# Procesar cada archivo .py
for archivo_py in archivos_py:
    # Obtener el nombre base del archivo sin la extensión
    nombre_base = os.path.splitext(archivo_py)[0]
    
    # Crear el objeto JSON para este par de archivos
    objeto = {
        "name": nombre_base,
        "prompt": "",
        "response": ""
    }
    
    # Ruta del archivo .txt correspondiente
    archivo_txt = os.path.join(directorio, nombre_base + '.txt')
    
    # Leer el contenido del archivo .txt
    with open(archivo_txt, 'r') as archivo:
        contenido_txt = archivo.read()
    
    # Ruta del archivo .py correspondiente
    archivo_py = os.path.join(directorio, archivo_py)
    
    # Leer el contenido del archivo .py
    with open(archivo_py, 'r') as archivo:
        contenido_py = archivo.read()
    
    # Asignar el contenido al objeto JSON
    objeto['prompt'] = contenido_txt
    objeto['response'] = contenido_py
    
    # Agregar el objeto JSON a la lista
    objetos_json.append(objeto)

# Escribir la lista de objetos JSON en el archivo final.json
with open('final.json', 'w') as archivo_json:
    json.dump(objetos_json, archivo_json, indent=4)
