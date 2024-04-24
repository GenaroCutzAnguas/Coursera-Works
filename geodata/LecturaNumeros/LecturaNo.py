import re

# Abre el archivo en modo lectura
with open(r'C:\Users\User\Desktop\Coursera-Works\geodata\LecturaNumeros\archivo.txt', 'r') as archivo:
    # Lee todas las líneas del archivo
    lineas = archivo.readlines()

# Inicializa la variable para almacenar la suma
suma = 0

# Itera sobre cada línea del archivo
for linea in lineas:
    # Utiliza re.findall() para encontrar todos los números en la línea
    numeros = re.findall(r'\d+', linea)
    
    # Convierte los números encontrados a enteros y suma
    suma += sum(map(int, numeros))

# Imprime el resultado
print(f"La suma de todos los números en el archivo es: {suma}")

