# EJERCICIOS LISTAS 

# Ejercicios manipulación

# 1. Consiste en la defición de una lista con elementos de diferentes tipos y en mostrarla por pantalla, tanto entera como por elementos accediento a la posición que ocupa dentro de la lista.
lista = ["Python", "Guanentá", 2022, "Libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de listas. Ademas, utilizar la función len paraconocer el numero de elementos que componen la lista.
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calcetines"]
print("Numero elementos lista1: ", len(lista1))
print("lista1: ", lista1)
print("Numero elementos lista2: ", len(lista2))
print("lista2: ", lista2)
lista_concatenada = lista1 + lista2
print("Numero elementos lista_concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas
lista = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersey","Sudadera"]
print(lista)
lista = lista + ["calcetines"] + ["Bufanda"]
print(lista)

# 4. Modificar elementos de una lista y borrar elementos de la misma
lista = ["Camiseta", "Pantalon", "Zapatillas"] 
print(lista)
lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)

