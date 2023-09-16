#Ejercicio 1 - Examen

def contar_letras(string):
    string = string.upper()
    cantidad_A = string.count('A')
    return cantidad_A

#Bloque principal
texto = input("Ingrese un texto: ")
cantidad_A = contar_letras(texto)
print(f"Cantidad de letras 'A' o 'a' mayusculas o minusculas: {cantidad_A}")
