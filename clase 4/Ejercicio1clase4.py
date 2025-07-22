monto_total = float(input("Ingrese el monto total de la cuenta:"))
propina_porcentaje = float(input("Ingrese el porcentaje de propina:"))

propina = monto_total * (propina_porcentaje /100)
total_final = propina + monto_total

print(f"El total a pagar es: {total_final}, El total de la propina que ya se encuentra en el precio final es de:{propina}")
