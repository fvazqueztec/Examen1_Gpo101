# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test Case 1
    (
        ["-85.5"],
        ["Total: ", 'Error en los datos'],
        ["Revisa las condiciones y mensajes cuando son datos inválidos"]
    ),
    # Test Case 2
    (
        ["750", "10"],
        ["Total: ", "Edad: ", 'Error en los datos'],
        ["Revisa las condiciones y mensajes cuando son datos inválidos"]
    ),
    # Test Case 3
    (
        ["750.15", "14"],
        ["Total: ", "Edad: ", 'Subtotal: 750.15',
            "Descuento: 37.51", "Total: 712.64"],
        ["Revisa las condiciones y mensajes cuando la edad es menor a 15 años"]
    ),
    # Test Case 4
    (
        ["750.15", "20"],
        ["Total: ", "Edad: ", "Subtotal: 750.15",
            "Descuento: 52.51", "Total: 697.64"],
        ["Revisa las condiciones y mensajes cuando la edad es par"]
    ),

    # Test Case 5
    (
        ["750.15", "21"],
        ["Total: ", "Edad: ", "Subtotal: 750.15",
            "Descuento: 67.51", "Total: 682.64"],
        ["Revisa las condiciones y mensajes cuando la edad es impar"]
    )
]
