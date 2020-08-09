## Palindromo 
palabra = input("Ingresa una palabra u oración, te diremos si es un palíndromo: ")
palabra = palabra.strip()
palabra_reves = palabra[::-1]
if palabra == palabra_reves:
    print("Tu palabra u oración es un palíndromo!") 
else:
    print("Tu palabra NO es un palíndromo")

print(palabra)
print(palabra_reves)