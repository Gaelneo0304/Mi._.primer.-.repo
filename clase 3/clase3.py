# colores = ["rojo", "verde", "azul"]
# print(f"Lista original: {colores}")

# colores[1] = "amarillo" # Cambiamos 'verde'
# print(f"Después de cambiar: {colores}")

# colores.append("violeta") # Añadimos al final
# print(f"Después de append: {colores}")

# color_eliminado = colores.pop(0) # Eliminamos 'rojo'
# print(f"Eliminamos {color_eliminado}, la lista queda: {colores}")



# lista_a = [1, 2, 3]
# lista_b = lista_a        # ¡Esto NO es una copia!
# lista_c = lista_a.copy() # ¡Esto SÍ es una copia!

# lista_b.append(4)

# print(f"Lista A: {lista_a}") # Se modificó también
# print(f"Lista B: {lista_b}")
# print(f"Lista C: {lista_c}") # Se mantuvo intacta


# numeros = [1, 2, 3, 4, 5]

# for num  in numeros:
#     print(f"prosesando numero: {num}")
#     print(num)
# # Ejemplo de uso de for en Python

# print (f"la lista tiene {len(numeros)} elementos.")
# print(f"¿esta el 4 en la lista? {4 in numeros}")

# numeros = [4, 1, 8, 1, 5]
# for num in numeros:  #num es una variable de iteracion
#     print(f"Procesando el número: {num}")  # f de format string
#     print(num)

# print(f"La lista tiene {len(numeros)} elementos.")
# print(f"¿Está el 8 en la lista? {8 in numeros}")
# numeros.sort() # Modifica la lista original
# print(f"Lista ordenada con .sort(): {numeros}")







#Actividad 
"""
Crea una lista vacía llamada playlist.
Pide al usuario que ingrese 3 nombres de canciones y añádelas a la lista usando append().
Muestra la playlist completa.
Muestra cuántas canciones hay en la playlist.
Pregunta al usuario qué canción quiere eliminar y quítala de la lista usando .remove().
Muestra la playlist final.
"""
#logica
"""
1.[]
2. tengo que poner un input para que el usuario ingrese los nombres de las canciones
3. print
4.len
5. que quiere eliminar con .remove()
6. print final
"""

# playlist = []
# for i in range (3):
#     cancion = input("Ingresa el nombre de una cancion:").capitalize()
#     playlist.append(cancion)
# print(f"Esta seria la playlist: {playlist} ")
# print(f"hay {len(playlist)} canciones en la playlist")
# cancion_eliminar = input("¿que cancion quieres eliminar?").capitalize()
# playlist.remove(cancion_eliminar)
# print(f"Esta es la playlist final: {playlist}")



# coordenadas = (1920, 1080,"Full HD")  # Tupla con ancho, alto y resolución
# # Desempaquetado

# ancho, alto, resolucion = coordenadas
# print(f"Ancho de la pantalla: {ancho}px")
# print(f"Alto de la pantalla: {alto}px")
# print(f"Resolución de la pantalla: {resolucion}")

# # También funciona en bucles for con listas de tuplas
# usuarios = [("juanperez", "juan@email.com"), ("ana_g", "ana@email.com")]
# for usuario, email in usuarios:
#     print(f"Procesando a {usuario} con email {email}")

# lenguaje = "Python"
# print(lenguaje[:])
#  #Acceso y slicing
# print(lenguaje[0])    # P
# print(lenguaje[-1])   # n
# print(lenguaje[1:4])  # yth
# # ¡Esto daría un error! Las cadenas son inmutables.
# #lenguaje[0] = "J"

lenguaje = "Alejandro Sosa-es un kpo"
# Acceso y slicing o rebanado
print(lenguaje[0])    # P
print(lenguaje[-2])   # n
print(lenguaje[1:10:3])  # yth  start - stop - step  == inico - fin - paso 
# ¡Esto daría un error! Las cadenas son inmutables.
#lenguaje[0] = "J"


