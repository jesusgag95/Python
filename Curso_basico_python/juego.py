import random


def adivina(numero):
    numero_adivina = int(input("Intenta adivinar el numero que estoy pensando (1-100): "))
    while numero != numero_adivina:
         if numero_adivina > numero:
             print("Te pasaste! el número que tengo en mente es menor, intentalo nuevamente")
         else:
             print("Te falta! el número que tengo en mente es mayor, intentalo nuevamente")
         numero_adivina = int(input("Escribe otro numero: "))
    print("Correcto! Estaba pensando en el número: " + str(numero))


def run():
    numero_aleatorio = random.randint(1,100)
    adivina(numero_aleatorio)


if __name__ == "__main__":
    run()