# Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : kevin@tepaz.com
# Fecha : 2022.09.28
# Editado 2022.09.28
valor=0
minimo=0
maximo=0
contador=0
primerNumero=True
while True:
    numero=input("ingrese un numero= ")
    if numero=="fin":
        break
    else:
        valor=valor+int(numero)
        contador=contador+1
    if (primerNumero):
        minimo = int(numero)
        maximo = minimo
        primerNumero = False
    else:
        if (int(numero) > maximo):
            maximo = int(numero)
        if (int(numero) < minimo):
            minimo= int(numero)      
print("Contador:", contador)
print("Suma:" , valor)
print("Promedio:", valor/contador)
print("Maximo:" , maximo)
print("Minimo:" , minimo)