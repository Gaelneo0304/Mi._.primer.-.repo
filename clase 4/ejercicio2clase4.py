nombre_completo = []
nombre_apellido_fecha = input("Ingrese su primer nombre, apellido y  la fecha de nacimiento(dd/mm/aaaa):").capitalize()
nombre_completo = nombre_apellido_fecha.split(" ")
nombre_suguerido = f"El nombre de usuario sugerido es:{nombre_completo[0][0:3]}{nombre_completo[1][0:3]}{nombre_completo[2][8:10]}".lower()
print(nombre_suguerido)
