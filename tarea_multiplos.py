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
