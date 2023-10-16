
# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento is None:
                print("n", end='\t')
            else:
                print(elemento, end='\t')
        print()

# Función para mostrar las coordenadas
def mostrar_coordenadas(coordenadas):
    for numero, coord in coordenadas.items():
        print(f"{numero}={coord}")

# Función para mostrar las coordenadas
def mostrar_coordenadasf(coordenadasf):
    for numerof, coordf in coordenadasf.items():
        print(f"{numerof}={coordf}")

# Función para realizar un movimiento hacia la izquierda
def mover_izquierda(matriz):
    n_x, n_y = -1, -1

    # Buscar la posición de "n" en la matriz
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == "n":
                n_x, n_y = i, j

    # Mover "n" a la casilla de la izquierda y el número en la casilla de la izquierda a la posición de "n"
    if n_x != -1 and n_y != -1 and n_y > 0:
        matriz[n_x][n_y], matriz[n_x][n_y - 1] = matriz[n_x][n_y - 1], matriz[n_x][n_y]

# Función para realizar un movimiento hacia la derecha
def mover_derecha(matriz):
    n_x, n_y = -1, -1

    # Buscar la posición de "n" en la matriz
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == "n":
                n_x, n_y = i, j

    # Mover "n" a la casilla de la derecha y el número en la casilla de la derecha a la posición de "n"
    if n_x != -1 and n_y != -1 and n_y < 2:
        matriz[n_x][n_y], matriz[n_x][n_y + 1] = matriz[n_x][n_y + 1], matriz[n_x][n_y]

# Función para realizar un movimiento hacia arriba
def mover_arriba(matriz):
    n_x, n_y = -1, -1

    # Buscar la posición de "n" en la matriz
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == "n":
                n_x, n_y = i, j

    # Mover "n" a la casilla de arriba y el número en la casilla de arriba a la posición de "n"
    if n_x != -1 and n_y != -1 and n_x > 0:
        matriz[n_x][n_y], matriz[n_x - 1][n_y] = matriz[n_x - 1][n_y], matriz[n_x][n_y]

# Función para realizar un movimiento hacia abajo
def mover_abajo(matriz):
    n_x, n_y = -1, -1

    # Buscar la posición de "n" en la matriz
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == "n":
                n_x, n_y = i, j

    # Mover "n" a la casilla de abajo y el número en la casilla de abajo a la posición de "n"
    if n_x != -1 and n_y != -1 and n_x < 2:
        matriz[n_x][n_y], matriz[n_x + 1][n_y] = matriz[n_x + 1][n_y], matriz[n_x][n_y]

# Función para verificar si la matriz está en el estado objetivo
def es_estado_objetivo(matriz):
    estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, "n"]]
    return matriz == estado_objetivo

# Algoritmo de resolución con búsqueda A*
def resolver_puzzle(matriz):
    movimientos = [mover_izquierda, mover_derecha, mover_arriba, mover_abajo]
    visitados = set()
    estado_inicial = (matriz, [])
    frontera = [estado_inicial]

    while frontera:
        estado, camino = frontera.pop(0)

        if es_estado_objetivo(estado):
            return camino

        visitados.add(str(estado))

        for movimiento in movimientos:
            nueva_matriz = [fila[:] for fila in estado]
            movimiento(nueva_matriz)

            if str(nueva_matriz) not in visitados:
                nuevo_camino = camino + [nueva_matriz]
                frontera.append((nueva_matriz, nuevo_camino))

    return None

# Crear una lista con los números del 1 al 8
numeros = list(range(1, 9))

# Establecer el número 7 en la posición (0,0)
matriz = [[7, 2, 4], [5, "n", 6], [8, 3, 1]]

# Mostrar el estado inicial
print("Estado inicial:")
mostrar_matriz(matriz)
print()

# Mostrar las coordenadas después del estado inicial
coordenadas = {
    1: (2, 2),
    2: (0, 1),
    3: (2, 1),
    4: (0, 2),
    5: (1, 0),
    6: (1, 2),
    7: (0, 0),
    8: (2, 0),
    "n": (1, 1)
}
#finales
# Mostrar las coordenadas después del estado inicial
coordenadasf = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    "n": (2, 2)
}
mostrar_coordenadas(coordenadas)
print()

# Resuelve el puzzle y muestra los pasos
print("Resolviendo el puzzle...")
pasos = resolver_puzzle(matriz)

if pasos:
    for i, paso in enumerate(pasos):
        print(f"Movimiento {i + 1}:")
        mostrar_matriz(paso)
        print()
else:
    print("No se encontró una solución.")

# Mostrar el estado final
if pasos:
    print("Estado final:")
    mostrar_matriz(pasos[-1])
    mostrar_coordenadasf(coordenadasf)
