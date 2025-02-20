"""" # Coloca los cuerpos de la solicitud POST en el archivo data.py  """

encabezado = {
    "Content-Type": "application/json" }

conj_min_de_datos = {
    "firstName": "ALY",
    "phone": "+15935553535",
    "address": "4994 Urdesa, Ave. VEEstrada, EC" }

kit_body = {
       "name": "Mi conjunto o kit ha sido creado" }


test_1_name_1 = "a"
"""
# PRUEBA 1.- El número permitido de caracteres (1): kit_body = { "name": "a"} #
# Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.# 
"""

test_2_name_511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
"""
# PRUEBA 2.- El número permitido de caracteres (511): kit_body = { "name": "El valor de prueba para esta comprobación será inferior a"} #
# Código de respuesta: 201. El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud #
# El número permitido de caracteres (511): kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}#
"""

test_3_name_0 = { "name": "" }
"""
# PRUEBA 3.- El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } #
# Código de respuesta: 400 #
"""

test_4_name_512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
"""
# PRUEBA 4.-	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name": "El valor de prueba para esta comprobación será inferior a” } #
# Código de respuesta: 400. El número de caracteres es mayor que la cantidad permitida (512): kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}#
"""

test_5_name_caractesp =  ("\"№%@\",")

"""
# PRUEBA 5.- Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } #
# Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. #
"""

test_6_name_espacios = { "name": " A Aaa " }
"""
# PRUEBA 6.- Se permiten espacios: kit_body = { "name": " A Aaa " } #
# Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. #
"""

test_7_name_numeros = { "name": "123" }
"""
# PRUEBA 7.- Se permiten números: kit_body = { "name": "123" } #
# Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud. #
"""

test_8_name_parametro_no_se_pasa_en_la_solicitud = { }
"""
# PRUEBA 8.- El parámetro no se pasa en la solicitud: kit_body = { } #
# Código de respuesta: 400. #
"""

test_9_name_parametro_diferente =  { "name": 123 }
"""
# PRUEBA 9.- Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } #
# Código de respuesta: 400 #
"""

""" DETALLES.-
# API Main User "Creacion de cuenta o usuario" 
#   Metodo POST - EndPoint /api/v1/users 
#   ENCABEZADO o HEADER 
encabezado = {
    "Content-Type": "application/json"
}
#   PARAMETROS.- Los parametros obligatorios son "firstname, phone y address", son strings 
#       El conjunto minimo de datos es  

conj_min_de_datos = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}
# La cuenta de usuario se ha creado correctamente- HTTP/1.1 201 Creado -{ authToken: 'jknnFApafP4awfAIFfafam2fma' } #
#
# API Main Kits "Crear un KIT" 
#   Metodo POST -  EndPoint /api/v1/kits 
#   ENCABEZADO O HEADER: 
#       Campo.- Authorization (string) 
#           Descripción.- Encabezado de autorización en formato Bearer {authToken}. 
#                     Cuando se pasa - se devuelven todos las cestas creadas por el usuario 
#       Campo.- Content-Type (string) 
#           Descripción.- Valor por defecto: application/json 
#   Ejemplo de ENCABEZADO o HEADER, el mismo que Creacion de usuario, SE LE HARA UN "COPY" 
#           { "Content-Type": "application/json" } 
#
#           { "Content-Type": "application/json", 
#                "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma" } 
#
#   PARAMETRO.- El parametro obligatorio es "name", es un string 
#   Respuesta.- El conjunto ha sido creado con exito

kit_body = {
       "name": "Mi conjunto o kit" }
"""