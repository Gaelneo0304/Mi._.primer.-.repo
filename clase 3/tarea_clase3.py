agenda = []  
for contacto in range(2):    #al definir un bucle for, se debe definir una variable de iteracion
    nombre = input("ingrese su nombre porfavor:").capitalize() #capitalize() convierte la primera letra en mayuscula, no converse paja
    telefono = input("ingrese su telefono porfavor:")
    contacto = (nombre, telefono)
    agenda.append(contacto)  # Agregar la tupla a la lista

print(agenda)  #mostrar la lista completa 
for nombre, telefono in agenda:
    print(f"Nombre: {nombre}, Telefono: {telefono}")


"""
##desde aca simplemente estaba probando cosas, cada parrafo es como la evolucion del anterior, Esto lo hice para ver que tanto podia hacer mientras estaba aburrido ⍤


usuario = input("Para saber si esta agendado, ingrese su nombre:").capitalize()
if usuario in [nombre for nombre, telefono in agenda]:
    print(f"El contacto {usuario} ya existe en la agenda.")
else:
    telefono_nuevo = input("El contacto no existe, porfavor ingrese el telefono:")
    nuevo_contacto = (usuario, telefono_nuevo)
    agenda.append(nuevo_contacto)
   
print(agenda)


verificacion = input("Desea agregar un contacto mas? (si/no): ").lower()
while verificacion == "si":   #bucle while, se ejecuta mientras la condicion sea verdadera
    nombre = input("ingrese su nombre:").capitalize()
    telefono = input("ingrese un telefono:")
    nuevo_contacto = (nombre, telefono)
    agenda.append(nuevo_contacto)
    verificacion = input("Desea agregar un contacto mas? (si/no): ").lower()
    if verificacion == "no":
        break     #break rompre el bucle 

for nombre, telefono in agenda:     #mostrar contactos guardados
    print(f"Nombre: {nombre}, Telefono: {telefono}")





verificacion = input("Desea agregar un contacto mas? (si/no): ").lower()
while verificacion == "si":   #bucle while, se ejecuta mientras la condicion sea verdadera
    nombre_nuevo = input("ingrese su nombre:").capitalize()
    if nombre_nuevo in [nombre for nombre, telefono in agenda]:
        print(f"El contacto {nombre_nuevo} ya existe en la agenda.")
    if nombre_nuevo not in [nombre for nombre, telefono in agenda]: #not in es para verificar si un elemento no esta en una lista
        telefono = input("ingrese un telefono:")
        nuevo_contacto = (nombre_nuevo, telefono)
        agenda.append(nuevo_contacto)
    verificacion = input("Desea agregar un contacto mas? (si/no): ").lower()
    if verificacion == "no":
        break     #break rompre el bucle 

for nombre, telefono in agenda:     #mostrar contactos guardados
    print(f"Nombre: {nombre}, Telefono: {telefono}")

"""


