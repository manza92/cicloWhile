condicion = 10

if condicion == True:
   print('Condicion verdadera')
elif condicion == False:
   print('Condicion falsa')
else:
   print('Condicion no reconocida')

numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto = ''
if numero == 1:
   numeroTexto = 'Numero uno'
elif numero == 2:
   numeroTexto = 'Numero dos'
elif numero == 3:
   numeroTexto = 'Numero tres'
else:
   numeroTexto = 'Valor fuera de rango'

print(f'Numero proporconado: {numero} - {numeroTexto}')

condicion = False

if condicion:
    print('Condicion verdadera')
else:
    print('Condicion falsa')
# para uso simplificado
print('Condicion verdadera') if condicion else print('Condicion falsa')

mes = int(input('Proporciona mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estacion es: {estacion}')

edad = int(input('Proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienzo el trabajo'
else:
    mensaje = 'Etapa de vida NO reconocida'
print(f'Tu edad es: {edad}, {mensaje}')

calificacion = int(input('Proporciona un valor entre 0 y 10: '))
notas = None

if 9 <= calificacion <= 10:
    notas = 'A'
elif 8 <= calificacion < 9:
    notas = 'B'
elif 7 <= calificacion < 8:
    notas = 'C'
elif 6 <= calificacion < 7:
    notas = 'D'
elif 0 <= calificacion < 6:
    notas = 'F'
else:
    notas = 'Valor incorrecto'
print(f'Tu nota {calificacion} es: {notas}')
