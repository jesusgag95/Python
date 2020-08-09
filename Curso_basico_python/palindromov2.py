def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra.lower()
    palabra_reves = palabra[::-1]
    if palabra == palabra_reves:
        return True
    else:
        return False


def run():
    palabra = input("escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()