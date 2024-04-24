import urllib.request, urllib.parse
import json, ssl

# URL de la API
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Solicitar al usuario la ubicación
address = 'Distant University of Hagen'

# Crear los parámetros de la consulta
parms = {'q': address}

# Crear la URL completa con los parámetros codificados
url = serviceurl + urllib.parse.urlencode(parms)

# Imprimir la URL recuperada
print('Retrieving', url)

# Abrir la URL y leer los datos
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

# Imprimir la cantidad de caracteres recuperados
print('Retrieved', len(data), 'characters')

try:
    # Convertir los datos JSON en un diccionario Python
    js = json.loads(data)
except:
    js = None

# Verificar si el diccionario contiene datos y la clave 'plus_code'
if js and 'features' in js and js['features'] and 'properties' in js['features'][0] and 'plus_code' in js['features'][0]['properties']:
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code:', plus_code)
else:
    print('No Plus Code Found')

