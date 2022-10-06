#Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : kevin@tepaz.com
# Fecha : 2022.09.22
# Editado 2022.09.22
cadena = "XDSPAM-CONDIDENDE:0.8475"
inicio=cadena.find(":")+1
final=len(cadena)
numero=float(cadena[inicio:final])
print (numero)
print(type(numero))