import ssl
import re
from urllib.request import urlopen

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1946849.html"
html = urlopen(url, context=ctx).read()

# Buscar números usando expresiones regulares
numbers = re.findall(r'<span class="comments">([0-9]+)</span>', html.decode())

# Convertir los números encontrados a enteros y sumarlos
total = sum(int(num) for num in numbers)

print("La suma de los números encontrados es:", total)
