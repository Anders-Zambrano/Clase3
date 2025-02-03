#Modificar el archivo de series.py y poner una función. Indicar los comentarios con sus nombres y apellidos.

# Archivo: series.py
# Modificado por: Andres Zambrano

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib