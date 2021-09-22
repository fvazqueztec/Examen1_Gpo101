# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["-5"],
        # Outputs
        ["Escribe un numero: ", "Error en los datos"],
        # Message in case of failure
        "Revisa los mensajes cuando el numero es negativo"
    ),
    # Test case 2
    (
        # Inputs
        ["10"],
        # Outputs
        ["Escribe un numero: ", "5"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado"
    ),
    # Test case 3
    (
        # Inputs
        ["13"],
        # Outputs
        ["Escribe un numero: ", "-7"],
        # Message in case of failure
        "Revisa que estes calculando bien tu resultado"
    ),
]
