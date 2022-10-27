# Ejercicios

# Manipulación

# Ejercicio 1

print("-------Ejercicio1-------------")

diassemanaingles = {"Lunes" : "Monday",
                    "Martes": "Tuesday",
                    "Miercoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}

print(diassemanaingles["Lunes"])
print(diassemanaingles["Miercoles"])
print(diassemanaingles["Viernes"])

# 2. Añade los días sábado y domingo, modificando el valor de algún elemento y borrando algún elemento.

print("----------Ejercicio 2--------------")

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}

print(diassemanaingles)
diassemanaingles["Sábado"] = "Saturday"
print(diassemanaingles)
diassemanaingles["Domingo"] = "Sunday"
print(diassemanaingles)
diassemanaingles["Lunes"] = "MondayBORRAR"
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)

# 3. Es posible utilizar las funciones len, max y min con los diccionarios. La primera devolverá el número de elementos que contiene el diccionario; la segunda, el elemento con el valor mayor y la tercera, el elemento con el valor menor. El valor mayor y el valor menor seá devueltos siempre que pueda calcularse dependiendo de los elementos que componen el diccionario.
()

print("-----------Ejercicio 3----------- ")

diassemanaingles = {"Lunes" : "Monday",
                   "Martes": "Tuesday",
                   "Miércoles" : "Wednesday",
                   "Jueves" : "Thursday",
                   "Viernes": "Friday"}
print("Número de elementos del diccionario: ", len(diassemanaingles))
print("Elemento mayor del diccionario: ",max(diassemanaingles))
print("Elemento menor del diccionario: ",min(diassemanaingles))


 
# FUNCIONES

print("-------Ejercicio 4 ------------")

diassemanaingles = {"Lunes" : "Monday",
                    "Martes": "Tuesday",
                    "Miercoles" : "Wednesday",
                    "Jueves" : "Thursday",
                    "Viernes" : "Friday"}
print("Diccionario original: ",diassemanaingles) 
# Función copy: Realiza una copia exacta del diccionario.
diccionariocopia = diassemanaingles.copy()
print("Diccionario copy: ",diccionariocopia)
# Funcióń pop: Obtiene el valor de la clave pasada como parametro y ademas elimina el elemento del diccionario.
print("Valor del lunes : ", diassemanaingles.pop("Lunes"))
print("Diccionario despues del pop: ",diassemanaingles)
# Función popitem: obtiene un aleatorioel diccionario y lo elimina del mismo.
print("Elemento al azar con popítem: ", diassemanaingles.popitem())
print("Diccionario despues del popitem: ",diassemanaingles)
# Funcion get: Obtiene el valor de la clave pasada como parametro.
print("Valor del Martes (get): ", diassemanaingles.get("Martes"))
print("Valor del Lunes (get) (no existe): ", diassemanaingles.get("Lunes"))
print("Valor del Lunes (get) (no existe): ", diassemanaingles.get("Lunes", "No existe"))
# Funcion uptade: Realiza una actualizacion del diccionario utilizando otro diccionario.
diassemanaingles.uptade({"Lunes":"MondayNUEVO","Martes":"TuesdayNuevo"})
print("Diccionario despues del uptade: ",diassemanaingles)
# Funcion setdefault:  Intenta insertar un elemento en el diccionario.
print("setdefault del sabado: ",diassemanaingles.setdefault("Sabado","saturday"))
print("Diccionario despues del setdefaul (nuevo elemento): ",diassemanaingles)
print("Setdefault del Lunes: " , diassemanaingles.setdefault("Lunes" , "Lunes"))
print("Diccionario después del setdefault (Elemento existente): " , diassemanaingles)
# Función Items: Devuelve un objeto iteravle (que puede utilizarse en bucles).
print("Elemento iterable (Items): " , diassemanaingles.items())
# Función Keys: Devuelve un objeto iteravle (que puede utilizarse en bucles) con las claves del diccionario.
print("Elemento iterable (Claves): " , diassemanaingles.keys())
# Función Values: Devuelve un objeto iteravle (que puede utilizarse en bucles) con los valores del diccionario.
print("Elemento iterable (Valores): " , diassemanaingles.values())
# Función Clear: Elimina todos los elementos .
print("Diccionario antes del clear: " , diassemanaingles)
print("Diccionario después del clear: " , diassemanaingles.clear())




