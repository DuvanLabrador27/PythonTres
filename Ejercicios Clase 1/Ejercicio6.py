#-----------------------CONVERSOR DE MONEDAS------------------------------

#--------------------------COP TO USD----------------------------------------------
menu="""
Bienvenido al conversor de monedas
1. Convertir de pesos colombianos a dolares
2. Convertir de dolares a pesos colombianos
"""
print(menu)



def copToUsd():
    peso_colombiano=float(input("¿Cuantos pesos colombianos tiene?: "))
    valor_dolar=4254

    dolar=peso_colombiano/valor_dolar
    dolar=round(dolar,2)
    print(f"Usted tiene ${dolar}".format(dolar))

#--------------------------FIN!!!------------------------------------------------------

#--------------------------USD TO COP----------------------------------------------
def usdToCop():
    dolar=float(input("¿Cuantos dolares USD tiene?: "))
    peso_colombiano=4254

    peso=dolar*peso_colombiano
    peso=round(peso,3)
    print(f"Usted tiene ${peso}".format(peso))

#--------------------------FIN!!!------------------------------------------------------
opcion = int(input("Ingrese la opcion que desea realizar: "))

if opcion==1:
    copToUsd()
elif opcion==2:
    usdToCop()
else:
    print("Opcion incorrecta")