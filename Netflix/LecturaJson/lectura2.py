import json
import sqlite3

# Ruta completa al archivo JSON
json_file_path = r'C:\Users\User\Desktop\Coursera-Works\Netflix\LecturaJson\roster_data.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE usuarios (
        nombre TEXT,
        codigo TEXT,
        numero INTEGER
    )
''')

for user in data:
    cursor.execute('INSERT INTO usuarios VALUES (?, ?, ?)', (user[0], user[1], user[2]))

# Consulta 1
query_1 = '''
    SELECT nombre, codigo, numero
    FROM usuarios
    ORDER BY nombre DESC, codigo DESC, numero DESC
    LIMIT 2;
'''


cursor.execute(query_1)


print("Resultado de la primera consulta:")
for row in cursor.fetchall():
    print("|".join(map(str, row)))

# Consulta 2
query_2 = '''
    SELECT 'XYZZY' || hex(nombre || codigo || numero) AS X
    FROM usuarios
    ORDER BY X
    LIMIT 1;
'''


cursor.execute(query_2)

result_2 = cursor.fetchone()
print("\nResultado de la segunda consulta:")
print(result_2[0])

conn.close()
