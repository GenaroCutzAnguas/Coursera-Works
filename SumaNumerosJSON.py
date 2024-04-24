import json
import urllib.request

# URL de los datos JSON
url = 'http://py4e-data.dr-chuck.net/comments_1946852.json'

# Obtener los datos JSON de la URL
response = urllib.request.urlopen(url)
data = response.read().decode()

# Cargar los datos JSON en un objeto Python
info = json.loads(data)

# Inicializar variables para contar y sumar los números
count = 0
total = 0

# Iterar sobre cada elemento en la lista 'comments'
for comment in info['comments']:
    count += 1  # Incrementar el contador de comentarios
    total += int(comment['count'])  # Sumar el valor 'count' convertido a entero

# Imprimir el total de comentarios y la suma de los números
print('Total de comentarios:', count)
print('Suma de los números encontrados:', total)
