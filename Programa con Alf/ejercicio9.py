inv_inicial = int(input("Ingrese el valor inicial del la inversion: "))
tasa_interes = float(input("Ingrese la tasa de interes anual(en potcentaje):"))
tiempo = int(input("Ingrese cuantos años desea invertir:"))
interes = inv_inicial * (tasa_interes / 100) * tiempo 
(print(f"El interes ganado en {tiempo} años es de: {interes}, dando un total de {inv_inicial + interes}")) 