# Ingresar datos
numero = input('Número: ')

# Convertir 
numero = int(numero)

# Solución 

residuo = numero % 10
numero = numero // 10
numeroInverso = residuo * 10

residuo = numero % 10
numero = numero // 10 
numeroInverso = (numeroInverso + residuo) * 10

residuo = numero % 10
numero = numero // 10 
numeroInverso = (numeroInverso + residuo) * 10

residuo = numero % 10
numero = numero // 10
numeroInverso = (numeroInverso + residuo) * 10

numeroInverso = numeroInverso + numero

# Salida de datos
print('Inverso: ', numeroInverso)
