import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
if len(url) < 1: quit()

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')

total = 0
for count in counts:
    total += int(count.text)

print('Count:', len(counts))
print('Sum:', total)