pan = 3.49
#pan viejo 60%

pan_viejo = pan * 0.6

pan_viejo_vendido = int(input("Cuantos panes viejos se vendieron hoy?: "))
# print(f"El total vendido de pan viejo de hoy fue de {pan_viejo_vendido} el precio normal es de {pan} y con el descuento es de {pan_viejo} ")
precio_total = pan_viejo * pan_viejo_vendido 
print(f"El total vendido fue de {pan_viejo_vendido} el precio normal es de {pan} por un pan, con descuento por pan es de {round(pan_viejo, 2)} y el total con descuento es de {round(precio_total, 2)}")
