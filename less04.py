
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
#imprimir la lista de nomres
print(nombres)
#acceder a los elementos de una lista

print(nombres[0])
print(nombres[1])
#acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-4])
#imprimir un rango

print(nombres[0:2]) # sin incluir el indice 2
# ir del inicio de la lista al indice sin incluirlo
print(nombres[:3])
#desde el indice indicado hasta el final
print(nombres[1:])
#cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')
#preguntar el largo de una lista
print(len(nombres))
#agregar un elemento
nombres.append('Hinata')
print(nombres)
#insertar un elemento en indice especifico
nombres.insert(1, 'Octavio')
print(nombres)
#remover un elemento
nombres.remove('Octavio')
print(nombres)
#remover ultimo valor agregado
nombres.pop()
print(nombres)
#eliminar un indice
del nombres[0]
print(nombres)
#limpiar la lista
nombres.clear()
print(nombres)
#borrar la lista por completo
del nombres
print(nombres)


# Definir una tupla

frutas = ('Naranja', 'Platano', 'Guayaba')
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a rango de valores
print(frutas[0:1]) #sin incluir ultimo indice
#recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor de una tupla
#frutas[0] = 'pera'
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n', frutas)
#eliminar la tupla
del frutas
print(frutas)

tupla = (13, 1, 8, 3, 2, 5, 8)
#Definir lista
lista = []
#Filtrar los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
#imprimimos la lista
print(lista)

# Set
planetas = {'Marte', 'Venus', 'Jupiter'}
print(planetas)
# largo de elemento
print(len(planetas))
# Revisar si un elemento esta presente
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print(planetas)
# no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elementos arrojando error
planetas.remove('Tierra')
print(planetas)
# Elimina un elemento sin dar error
planetas.discard('Jupiters')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar set
del planetas
print(planetas)
