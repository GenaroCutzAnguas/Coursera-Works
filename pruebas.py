# Crear el diccionario de precios
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, 'ciruela': 2.45, 'durazno': 4.55, 'melon': 7.35, 'sandia': 9.70, 'anana': 11.25}

# Cantidad de cada fruta en el ticket de compra
compra = {'manzana': 2, 'banana': 2.5, 'kiwi': 1, 'pera': 3, 'ciruela': 1, 'durazno': 2, 'melon': 5, 'sandia': 10, 'anana': 3}

# Calcular el precio del ticket de compra
precio_total = sum(precios[fruta] * cantidad for fruta, cantidad in compra.items())

# Imprimir el resultado
print(f"El precio total del ticket de compra es: ${precio_total:.2f}")
