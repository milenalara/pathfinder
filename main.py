import heapq

def heuristica(a, b):
    """Distância de Manhattan"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def encontrar_ponto(matriz, ponto):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == ponto:
                return (i, j)
    return None

def vizinhos(pos, matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    resultado = []

    for dx, dy in movimentos:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < linhas and 0 <= ny < colunas and matriz[nx][ny] != 1:
            resultado.append((nx, ny))
    return resultado

def a_estrela(matriz):
    start = encontrar_ponto(matriz, 'S')
    end = encontrar_ponto(matriz, 'E')

    if not start or not end:
        return "Erro: Ponto inicial ou final ausente."

    fila = [(0 + heuristica(start, end), 0, start, [start])]
    visitados = set()

    while fila:
        f, g, atual, caminho = heapq.heappop(fila)

        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == end:
            return caminho

        for viz in vizinhos(atual, matriz):
            if viz not in visitados:
                novo_g = g + 1
                novo_f = novo_g + heuristica(viz, end)
                heapq.heappush(fila, (novo_f, novo_g, viz, caminho + [viz]))

    return "Sem solução"

def mostrar_caminho(matriz, caminho):
    resultado = [linha.copy() for linha in matriz]
    for x, y in caminho:
        if resultado[x][y] not in ('S', 'E'):
            resultado[x][y] = '*'
    return resultado

def imprimir_matriz(matriz):
    for linha in matriz:
        print(' '.join(str(cell) for cell in linha))

# Exemplo de uso
labirinto = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1],
]

caminho = a_estrela(labirinto)
if isinstance(caminho, str):
    print(caminho)
else:
    print("Caminho encontrado (coordenadas):")
    print(caminho)
    print("Labirinto com caminho:")
    imprimir_matriz(mostrar_caminho(labirinto, caminho))
    