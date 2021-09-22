![Tec de Monterrey](../../images/logotecmty.png)
# Super mercado

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe aquí tu código
    

if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

El siguiente algoritmo se puede usar para determinar la cantidad a pagar en un supermercado, considerando el siguiente orden de entradas:

   * Si el total de la compra es 0 o menor que 0, se debe indicar "Error en los datos"
   * Si el total de la compra es menor a 100.00 pesos, entonces el programa ya no debe continuar, se muestra el total y el mensaje "Sin descuento".  
   * Solicitar la edad del usuario (en años cumplidos), si la edad de usuario es 12 o menor que 12, se debe indicar "Error en los datos"
   * Si la edad del usuario es menor a 15 años, se le aplica un 5% de descuento a la compra, por lo que el programa deberá mostrar el subtotal, descuento y total a pagar, las cantidades deberan estar redondeadas a 2 dígitos. Recuerda utilizar la instrucción round(cantidad, 2)
   * Si la edad del usuario es par, entonces, se le aplica el 7% de descuento, por lo que el programa deberá mostrar el subtotal, descuento y total a pagar, las cantidades deberan estar redondeadas a 2 dígitos. Recuerda utilizar la instrucción round(cantidad, 2) 
   * Si la edad del usuario es impar, entonces, se le aplica el 9% de descuento, por lo que el programa deberá mostrar el subtotal, descuento y total a pagar, las cantidades deberan estar redondeadas a 2 dígitos. Recuerda utilizar la instrucción round(cantidad, 2) 

**Entradas**  
Total
Edad (solo si el total es mayor o igual que 100 pesos)

  
**Salidas**  
Si el total es menor o igual que cero, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Si el total es menor a 100.00 pesos, deberá mostrar el total a pagar y el mensaje: 
    **Sin descuento**
Si se solicitó la edad y es menor o igual que 12, deberá mostrar el siguiente mensaje: 
    **Error en los datos**
Si el total y la edad son válidos, deberá motrar el siguiente mensaje: 
 
## Ejemplos  

Ejemplo 1    

```plaintext
Total: 75.50
Sin descuento
```

Ejemplo 2

```plaintext
Total: -45.23
Error en los datos
```

Ejemplo 3

```plaintext
Total: 195.12
Edad: 5
Error en los datos
```

Ejemplo 4

```plaintext
Total: 575.43
Edad: 14
Subtotal: 575.43
Descuento: 28.77
Total: 546.66
```

Ejemplo 4

```plaintext
Total: 850
Edad: 43
Subtotal: 850.0
Descuento: 76.5
Total: 773.5
```


**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.
