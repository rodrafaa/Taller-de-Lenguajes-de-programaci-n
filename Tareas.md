# Bitacora de clase

## Parcial 1
1. Tarea #998 - Crear una key ssh en git bash ✅
![Alt text](https://github.com/rodrafaa/Taller-de-Lenguajes-de-programaci-n/blob/main/image.png?raw=true)

2. Tarea #997 - Tarea del libro ✅

```python
def is_multiple(n, m):
    # n es múltiplo de m si el residuo es 0
    return n % m == 0

# Pedimos los datos al usuario para que sea interactivo
try:
    print("--- Verificador de Múltiplos ---")
    num_n = int(input("Introduce el número n: "))
    num_m = int(input("Introduce el número m: "))

    if is_multiple(num_n, num_m):
        print(f"✅ ¡Sí! {num_n} es múltiplo de {num_m}.")
    else:
        print(f"❌ No, {num_n} no es múltiplo de {num_m}.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Por favor introduce solo números enteros.")
```
3. Tarea #996 - Tarea del libro ✅

```python
def contar_divisiones(n):
    """
    Cuenta cuántas veces se puede dividir n entre 2 antes de ser < 2.
    Esto es una implementación práctica para visualizar el concepto 
    de logaritmo base 2.
    """
    if n <= 2:
        return 0
    
    contador = 0
    valor_actual = n
    
    while valor_actual >= 2:
        valor_actual = valor_actual / 2
        contador += 1
        
    return contador

if __name__ == "__main__":
    print("--- Calculadora de Divisiones Logarítmicas ---")
    try:
        numero = int(input("Introduce un número entero mayor que 2: "))
        
        if numero <= 2:
            print("Por favor, introduce un número estrictamente mayor que 2.")
        else:
            resultado = contar_divisiones(numero)
            print(f"El número {numero} se dividió {resultado} veces antes de ser menor que 2.")
            
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
 ```
