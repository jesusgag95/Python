def conversor(tipo_peso, valor_dolar):
    pesos = float(input("Cuantos pesos " + tipo_peso + " tienes?: "))
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    return dolares

pesos_convertir = int(input("Introduce 1 si quieres convertir pesos mexicanos, 2 para colombianos, 3 para argentinos: "))

if pesos_convertir == 1:
    resultado = conversor("Mexicanos",22.28)
elif pesos_convertir == 2:
    resultado = conversor("Colombianos",3691.20)
elif pesos_convertir == 3:
    resultado = conversor("Argentinos",71.84)
else:
    print("Ingresa un valor correcto ")
    
    
print("Tienes " + str(resultado) + " Dolares")