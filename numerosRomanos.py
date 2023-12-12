def convertir_a_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    i = 0
    while numero > 0:
        if numero >= valores[i]:
            resultado += romanos[i]
            numero -= valores[i]
        else:
            i += 1
    return resultado

# Programa principal
while True:
    entrada = input("Ingresa un número entero (0 para salir): ")
    if entrada == "0":
        print("¡Hasta luego!")
        break
    try:
        numero = int(entrada)
        if numero <= 0:
            print("Ingresa un número entero positivo.")
        else:
            romano = convertir_a_romano(numero)
            print(f"El número {numero} en números romanos es: {romano}")
    except ValueError:
        print("Ingresa un número entero válido.")