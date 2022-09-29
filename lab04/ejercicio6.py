# Tendencias e innovacion en Tecnologia Agricola (TEA)
# Autor : kevin@tepaz.com
# Fecha : 2022.09.22
# Editado 2022.09.22

def calcularpago(horas,tarifa):
    MAX_HORAS_SEMANALES=40
    horas_extras=0
    if(horas>MAX_HORAS_SEMANALES):
        horas_extras = horas-MAX_HORAS_SEMANALES
        horas= MAX_HORAS_SEMANALES
    calculo= (horas*tarifa)+(horas_extras*(tarifa * 1.5))
    return calculo 
horas=int(input("ingrese numero de horas= "))
tarifa=int(input("ingrese numero de tarifa= "))
pago= calcularpago(horas,tarifa)
print(pago)

     