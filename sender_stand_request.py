""""  # Todas las solicitudes que necesitas, se pueden almacenar en el archivo sender_stand_request.py #  """
import configuration
import requests
import data

"""# Envío de la solicitud POST: para enviar la solicitud, utiliza la función post() #"""
def post_crear_nuevo_usuario(body):
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,                 #inserta el cuerpo de solicitud #
                             headers=data.encabezado)   #inserta los encabezados #

print("\n Soy la funcion -CREAR NUEVO USUARIO-")
print(data.conj_min_de_datos)
print(data.encabezado)

def post_new_client_kit(kit_body, auth_token):
        actual_encabezado = data.encabezado.copy()
        actual_encabezado["Authorization"] = "Bearer " + auth_token
        return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=actual_encabezado)

print("\n 'Soy la funcion -CREAR NUEVO KIT-")
print(data.kit_body)
print(data.encabezado)



""" Detalle.- 
# Envío de la solicitud POST: para enviar la solicitud, utiliza la función post() #
# de la librería Requests de Python. #
# Esta función necesita la URL completa, el cuerpo de la solicitud y los encabezados:#
# Envía una solicitud para crear un nuevo usuario y recuerda el token de autenticación (authToken) # 

def post_crear_nuevo_usuario(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # inserta el cuerpo de solicitud #
                         headers=data.encabezado)  # inserta los encabezados #

print("\n Soy la funcion -CREAR NUEVO USUARIO-")
print(data.conj_min_de_datos)
print(data.encabezado)

# Envía una solicitud para crear un kit para este usuario. Asegúrate de pasar también el encabezado Autorization #
# La función para crear un nuevo kit se denominara post_new_client_kit #

def post_new_client_kit(kit_body, auth_token):
    actual_encabezado = data.encabezado.copy()
    actual_encabezado["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=actual_encabezado)


print("\n 'Soy la funcion -CREAR NUEVO KIT-")
print(data.kit_body)
print(data.encabezado)
print(post_new_client_kit())

 Utiliza dos parámetros en la función para crear un nuevo kit: 
 kit_body (el cuerpo de solicitud) y auth_token (el token de autenticación)
 Y data.encabezado.copy()-- copia la solicitud para crear un nuevo usuario sobre solicitudes POST 

 Son dos funciones:
    La primera funcion es para crear el usuario y
 obtener el authoken
 y ese atuhoken lo debo pasar en el header de 
 la siguiente peticion post new client
 esta peticion necesita el athoken en el header
 para poder crear el kit
"""


