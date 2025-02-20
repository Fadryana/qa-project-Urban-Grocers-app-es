""""# La lista de comprobación completa debe estar en el archivo create_kit_name_kit_test.py # """
import sender_stand_request
import data

"""# Puedes crear una función que cambiará el contenido del cuerpo de solicitud, nómbrala get_kit_body y agrega el parámetro "name" #
"""
def get_kit_body(name):
    actual_kit_body = data.kit_body.copy()
    actual_kit_body["name"] = name
    return actual_kit_body

"""# Recibir el token también puede ser una función separada.   Llámala get_new_user_token() #"""

def get_new_user_token():
    conj_minimo_de_datos = data.conj_min_de_datos
    response = sender_stand_request.post_crear_nuevo_usuario(conj_minimo_de_datos)
    return response.json()["authToken"]

"""# Hay dos tipos de pruebas en la lista de comprobación: POSITIVAS Y NEGATIVAS #
# TIPO DE PRUEBA POSITIVA - Su lógica se puede expresar en funcion: positive_assert(kit_body) # """

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    print(f" El status codigo recibido es: {response.status_code}")
    assert response.status_code == 201  # 201 SE HA CREADO # "Comprueba que el resultado es 201". #
    assert response.json()["name"] == kit_body["name"]


def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    print(f" El status codigo recibido es: {response.status_code}")
    assert response.status_code == 400   # Status_code es el Código de respuesta #


def test_create_user_1_letter_in_kit_get_success_response():
    body_actual = get_kit_body(data.test_1_name_1)
    positive_assert(body_actual)
    print("Ese fue el resultado para este  body actual: " , body_actual)


def test_create_user_511_letter_in_kit_get_success_response():
    body_actual2 = get_kit_body(data.test_2_name_511)
    positive_assert(body_actual2)
    print("Ese fue el resultado para este  body actual: ", body_actual2)


def test_create_user_0_letter_in_kit_get_success_response():
    body_actual3 = get_kit_body(data.test_3_name_0)
    negative_assert_400(body_actual3)
    print("Ese fue el resultado para este  body actual: ", body_actual3)


def test_create_user_512_letter_in_kit_get_success_response():
    body_actual4 = get_kit_body(data.test_4_name_512)
    negative_assert_400(body_actual4)
    print("Ese fue el resultado para este  body actual: ", body_actual4)


def test_create_user_caract_espec_in_kit_get_success_response():
    body_actual5 = get_kit_body(data.test_5_name_caractesp)
    positive_assert(body_actual5)
    print("Ese fue el resultado para este  body actual: ", body_actual5)


def test_create_user_espacios_in_kit_get_success_response():
    body_actual6 = get_kit_body(data.test_6_name_espacios)
    positive_assert(body_actual6)
    print("Ese fue el resultado para este  body actual: ", body_actual6)


def test_create_user_numeros_in_kit_get_success_response():
    body_actual7 = get_kit_body(data.test_7_name_numeros)
    positive_assert(body_actual7)
    print("Ese fue el resultado para este  body actual: ", body_actual7)


def test_create_user_param_no_pasa_in_kit_get_success_response():
    body_actual8 = get_kit_body(data.test_8_name_parametro_no_se_pasa_en_la_solicitud)
    negative_assert_400(body_actual8)
    print("Ese fue el resultado para este  body actual: ", body_actual8)


def test_create_user_paramdiferente_in_kit_get_success_response():
    body_actual9 = get_kit_body(data.test_9_name_parametro_diferente)
    negative_assert_400(body_actual9)
    print("Ese fue el resultado para este  body actual: ", body_actual9)


"""# La palabra clave ASSERT(afirmar), funciona como una expresión lógica porque devuelve True o False.#

# Hay dos tipos de pruebas en la lista de comprobación: POSITIVAS Y NEGATIVAS #
# TIPO DE PRUEBA NEGATIVA (código 400) - Su lógica se puede expresar en funcion: negative_assert_code_400(kit_body) # 
"""

"""
Se usan dos funciones mas  possitive assert y negative assert.
    - El positive assert hace la peticion 
        y revisa que el resultado sea un 200
        es una prueba positiva

    - EL negative assert hace la peticion 
       y revisa que el resultado sea un 400
       es una prueba negativa
     """

"""
# Se especifican los archivos y directorios para iniciar Pytest #
# La búsqueda no distingue entre mayúsculas y minúsculas, por lo que puede encontrar tanto Test_1.py como test_1.py#
#   Cada prueba debe estar en una función separada con el prefijo test, de lo contrario, Pytest las ignorará #
# test_create_user_2_letter_in_first_name_get_success_response(). #
"""
