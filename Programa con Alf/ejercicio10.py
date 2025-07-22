payaso = 122
muñeca = 75
payasos_vendido = int(input("Ingrese la cantidad de payasos vendidos: "))
muñecas_vendidas = int(input("Ingrese la cantidad de muñecas vendidas: "))
peso_payaso = payaso * payasos_vendido
peso_muñeca = muñeca * muñecas_vendidas
peso_total = peso_payaso + peso_muñeca
valor_peso = int(input("Ingrese el valor del peso del correo: "))
costo_envio = peso_total * valor_peso
print(f"El costo del envio es de {costo_envio} pesos, con un peso total del envio de {peso_total} gramos.")