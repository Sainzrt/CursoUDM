print("hola a todos")

def imprimir_y_multiplicar_por_dos(dato):
    if not isinstance(dato, (int, float)):
        print("Error: Solo se permiten números (int o float).")
        return
    print(f"Dato recibido: {dato}")
    resultado = dato * 2
    print(f"Resultado de multiplicar por 2: {resultado}")

# Ejemplo de uso
imprimir_y_multiplicar_por_dos("5")