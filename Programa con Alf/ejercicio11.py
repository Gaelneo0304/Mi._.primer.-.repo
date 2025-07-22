# inversion_inicial = int(input("Cuanto desea invertir?: "))
# tasa_anual = 4
# tiempo =int(input("Cuantos años desea invertir?: "))
# for i in range(tiempo):
#     inversion_inicial = inversion_inicial * (1 + tasa_anual / 100) 
#     inversion_inicial = round(inversion_inicial, 2)


# print(inversion_inicial)


inversion_inicial = int(input("Cuanto desea invertir?: "))
tasa_anual = 4

primer_año = inversion_inicial * (1 + tasa_anual / 100)
print(f"Balance del primer año: {primer_año}")

segundo_año = primer_año * (1 + tasa_anual / 100)
print(f"Blance del segundo año: {segundo_año}")

tercer_año = segundo_año * (1 + tasa_anual / 100)
print(f"Balance del tercer año: {tercer_año}")