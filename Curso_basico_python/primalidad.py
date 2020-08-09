def pedir_num():
    numero = input("Ingresa un numero, te diremos si es primo: ")
    return numero


def es_primo(numero):
    contador = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            contador += 1

    
    if contador == 2:
        return True
    else:
        return False


def run():
    numero = int(pedir_num())
    primo = es_primo(numero)
    if primo == True:
        print("Tu numero es primo!")
    else:
        print("Tu numero NO es primo :( ")


if __name__ == "__main__":
    run()