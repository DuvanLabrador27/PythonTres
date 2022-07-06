def conversor_pesoToUsd(tipo_moneda,valor_dolar):
    peso = float(input("¿Cuantos pesos " + tipo_moneda+" tienes disponible?: "))
    dolar=peso/valor_dolar
    dolar=round(dolar,2)
    print(f"Usted tiene ${dolar}".format(dolar))

def conversor_usdToPeso(tipo_moneda,valor_peso):
    dolar = float(input("¿Cuantos dolares " + tipo_moneda+" tienes disponible?: "))
    peso=dolar*valor_peso
    peso=round(peso,3)
    print(f"Usted tiene ${peso}".format(peso))

menu="""
Bienvenidos al conversor de monedas
1. Convertir de COP A USD
2. Convertir de USD A COP
3. Convertir de ARG A USD
4. Convertir de USD A ARG
5. Convertir de MEX A USD
6. Convertir de USD A MEX

"""    
print(menu)
opcion = int(input("Ingrese la opción: "))

if opcion==1:
    conversor_pesoToUsd("Colombianos",4252)
elif opcion==2:
    conversor_usdToPeso("Dolares",4252)
elif opcion==3:
    conversor_pesoToUsd("Argentinos",65)
elif opcion==4:
    conversor_usdToPeso("Dolares",65)
elif opcion==5:
    conversor_pesoToUsd("Mexicanos",24)
elif opcion==6:
    conversor_usdToPeso("Dolares",24)













































