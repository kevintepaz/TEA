#Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : kevin@tepaz.com
# Fecha : 2022.10.05
# Editado 2022.10.05
try:
  entrada = input("ingrese el nombre del archivo: ")
  archivo = open(entrada)
  for linea in archivo:
    print(linea.upper())
except:
     print("error, no existe el archivo")
