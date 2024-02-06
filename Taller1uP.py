from array import array
def elem(A, i, j):
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        return None  # Índices fuera de rango para una matriz 3x3
    
    indice = i * 3 + j
    return A[indice]

# Ejemplo de uso:
A = array ('f',[1, 2, 3, 4, 5, 6, 7, 8, 9])  # Array que representa una matriz de 3x3
i = 2
j = 1
elemento = elem(A, i, j)
print(f"El elemento en la posición ({i}, {j}) es: {elemento}")  # Debería imprimir: El elemento en la posición (1, 2) es: 6
