import json
import sqlite3

# Ruta completa al archivo JSON
json_file_path = r'C:\Users\User\Desktop\Coursera-Works\Netflix\LecturaJson\roster_data.json'

# Lee el archivo JSON
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Crea una base de datos en memoria
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Crea una tabla para almacenar la información
cursor.execute('''
    CREATE TABLE usuarios (
        nombre TEXT,
        codigo TEXT,
        numero INTEGER
    )
''')

# Inserta los datos en la tabla
for user in data:
    cursor.execute('INSERT INTO usuarios VALUES (?, ?, ?)', (user[0], user[1], user[2]))

# Guarda los cambios y cierra la conexión
conn.commit()
conn.close()
