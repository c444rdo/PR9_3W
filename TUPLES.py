print ("Martínez Estrada Ricardo")
print (" ")

# Las tuplas/tuples es una forma de almacenar varios items en una sola variable, similar a las lists/listas.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print (" ")

# Las tuplas/tuples permiten almacenar variables repetidas.
thistuple2 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple2)
print (" ")

# Para determinar cuantos items tiene una tupla, podemos usar la función (len(x))
thistuple3 = ("apple", "banana", "cherry")
print(len(thistuple3))
print (" ")

# Para crear una tupla de un solo item, tenemos que rodearla de comillas y al finalizar poner una comilla.
# De lo contrario Python no lo reconocerá como una tupla.
thistuple4 = ("apple",)
print(type(thistuple4))
print (" ")

# Las tuplas pueden ser cualquier tipo de dato.
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Una tupla puede contener diferentes tipos de datos.
tuple4 = ("abc", 34, True, 40, "male")

# Podemos averiguar el tipo de dato que contiene una dupla utilizando la función (type(x))
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))