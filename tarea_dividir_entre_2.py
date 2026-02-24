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
 
