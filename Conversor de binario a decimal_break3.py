binario = str(input("Introduce un número binario: "))

posicion = 0
decimal = 0
conversionOK = True

for n in reversed(binario):
    if n != "0" and n != "1":
        conversionOK = False
        break
    else:
        decimal += int(n)*(2**posicion)
        posicion += 1

if conversionOK:
    print(decimal)
else:
    print("No es un número binario. Introduce 0 y 1")