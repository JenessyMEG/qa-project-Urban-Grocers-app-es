import sender_stand_request
import data

def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body

#========================================================================================================

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201

# Función de prueba negativa
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si la respuesta contiene el código 400.
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "kit name's is empty "

def negative_assert_no_name(name):
    kit_body = get_kit_body(name)
    # Guarda el resultado de llamar a la función a la variable "kit_response"
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    assert kit_response.status_code == 400

    assert kit_response.json()["code"] == 400
 y data
    assert kit_response.json()["message"] == "No se enviaron todos los parámetros requeridos"

# Prueba 1. El número permitido de caracteres (1)

def test_1_one_character_name_get_success_response():
    positive_assert("a")

# Prueba 2. El número permitido de caracteres (511)
def test_2_allowed_numbers_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3: El número de caracteres es menor que la cantidad permitida (0):
def test_3_zero_number_characteres_name_get_error_response():
    negative_assert_no_name("")

#Prueba 4. El número de caracteres es mayor que la cantidad permitida (512):
def test_4_greater_number_characteres_name_get_error_response():
    negative_assert_no_name ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5. Se permiten caracteres especiales:
def test_5_spacial_characteres_name_get_success_response():
    positive_assert("%@")

#Prueba 6. Se permiten espacios:
def test_6_spacial_name_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7.  Se permiten números:
def test_7_number_passed_name_get_success_response():
    positive_assert("123")

#Prueba 8. El parámetro no se pasa en la solicitud:
def test_8_parameter_not_passed_name_get_error_response():
    negative_assert_no_name("")

#Prueba 9. Se ha pasado un tipo de parámetro diferente (número):
def test_9_diferent_parameter_name_get_error_response():
    negative_assert_no_name(123)
