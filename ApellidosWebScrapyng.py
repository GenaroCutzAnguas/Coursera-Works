import urllib.request
import re
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Realizar el rastreo y extracción de enlaces
for _ in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url, context=ctx).read().decode()
    links = re.findall(r'href="(http[s]?://.*?)"', html)
    url = links[position - 1]

print("Last URL in sequence:", url)
