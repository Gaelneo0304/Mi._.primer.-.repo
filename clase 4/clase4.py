#paso 1 importar las librerias para comunicarnos con internet
import requests 

#paso 2 recolectar cada dato y guardarlo en su propia variable

nombre = input("Ingrese su nombre:")
fecha = input("Ingrese la fecha:")
email = input("Ingrese su mail:")

#paso 3 definir la url del servicio web
url_webhook = "https://hook.us2.make.com/cyvem4ppnv6ql8nkjo806gkvq59d754a"

#paso 4 Organizamos los datos en un diccionario

datos_a_enviar = {
    "name": nombre,
    "startDate": fecha,
    "email": email 
}

#paso 5 Enviamos  los datos al webhook
print("enviando informacion")
respuesta = requests.post(url=url_webhook, json=datos_a_enviar)

#paso 6 Mostramos la respuesta del servidor para ver si todo salio bien

print(f"Status: {respuesta.status_code}")
print(f"Respuesta del servidor:{ respuesta.text}")



