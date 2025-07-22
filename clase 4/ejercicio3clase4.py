lista = ["Leche", "Pan", "Huevos"]

producto_nuevo = input("Ingrese otro producto a la lista:").capitalize()
lista.append(producto_nuevo)

producto_nuevo2 = input("Ingrese otro producto a la lista:").capitalize()
lista.insert(0, producto_nuevo2)

print(f"La lista se compone de: {lista} y contiene {len(lista)} productos")
lista.sort()

producto_eliminar = input("Que producto desea eliminar de la lista:").capitalize()
lista.remove(producto_eliminar)
print(f"La lista final se comopone de :{lista}, ahora contiene {len(lista)} productos")
