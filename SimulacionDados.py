import random

def tirar_dados():
    while True:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        print(f"Dado 1: {dado1} | Dado 2: {dado2}")
        print(f"Suma de los dados: {suma}")
        otra_vez = input("¿Quieres tirar los dados otra vez? (s/n): ").lower()
        if otra_vez != 's':
            break

if __name__ == "__main__":
    tirar_dados()