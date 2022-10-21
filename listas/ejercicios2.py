# EJERCICIOS LISTAS 

# Métodos propios

lista = [45, 32, 3, 78]
print("lista original: ", lista)
# Funcion append: añade un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista despues de usar append: " , lista)
# Funcion sort: Ordena lista
lista.sort()
print("Lista ordenada: ", lista)
# Funcion reverse: Invite el orden de la lista
lista.reverse()
print("Lista al reves: ", lista)
# Función extend: añade los elementos de una lista a la lista
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend: ", lista)
# Función count: Cuenta el numero de veces que aparece el elemento indicado como parámetro de la lista
print("Numero de elementos 45: ", lista.count(45))
# Función insert: Añade el elemento pasado como parámetro a la lista en la posición indicada tambien por parametro
lista.insert(4,111)
print("Lista despues de insert: ", lista)
# Función remove: Elimina la primera ocurrencia empezando por la izquierda de la lista del elemento indicado como parametro.
lista.remove(45)
print("Lista despues de remove: ", lista)
# Función index: Devuelve la posición de la primera ocurrencia de izquierda  a derecha en la lista, del elemento pasado como parametro.
print("Posicion del elemento 111: ",lista.index(111))
# funcion pop: Elimina el ultimo elemento de la lista y lo devuelve como resultado de la operacion.
lista.pop()
print("Lista despues de pop ", lista)
# Fucion clear: Elimina todos los elementos de la lista.
lista.clear()
print("Lista despues de clear: ", lista)