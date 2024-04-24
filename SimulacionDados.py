import random

def tirar_dados():
    moneda = random.randint(1, 2)
    
    if(moneda == 1):
        print("Cara")
    else:
        print("Sol")

if __name__ == "__main__":
    tirar_dados()
    