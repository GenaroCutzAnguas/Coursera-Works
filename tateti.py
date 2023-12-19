import sys

# Función para mostrar la tabla del juego
def mostrar_tabla(tabla):
    for i in range(3):
        for j in range(3):
            print(tabla[i][j], end=' ')
        print()

# Función para verificar si hay una victoria o si hay un empate
def verificar_estado(tabla):
    # Verificar si hay una victoria en filas, columnas o diagonales
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != 0:
            return True, tabla[i][0]
        if tabla[0][i] == tabla[1][i] == tabla[2][i] != 0:
            return True, tabla[0][i]

    # Verificar si hay una victoria en las diagonales
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != 0:
        return True, tabla[0][0]
    if tabla[0][2] == tabla[1][1] == tabla[2][0] != 0:
        return True, tabla[0][2]

    # Verificar si hay un empate (si no hay casillas vacías)
    for i in range(3):
        for j in range(3):
            if tabla[i][j] == 0:
                return False, 0

    return True, 'E'

# Función principal del juego
def main():
    tabla = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    turno = 1

    while True:
        mostrar_tabla(tabla)
        print("Turno del jugador", turno)
        print("Ingrese las coordenadas (separadas por un espacio) para colocar su ficha:")
        try:
            fila, columna = map(int, input().split())
            if not (1 <= fila <= 3) or not (1 <= columna <= 3):
                raise ValueError("Ingrese un valor dentro del rango permitido (1-3).")

            if tabla[fila-1][columna-1] != 0:
                print("Casilla ocupada. Ingrese otro valor.")
                continue

            tabla[fila-1][columna-1] = turno

            # Verificar si hay una victoria o un empate
            estado, ganador = verificar_estado(tabla)

            if estado:
                if ganador == 'E':
                    print("Empate.")
                else:
                    print("Ganador del juego: jugador", ganador)
                break

            turno = 3 - turno
        except ValueError as ve:
            print("Error:", ve)

# Ejecutar el juego
main()