# Projeto Path Finder

Aluna: Milena Lara Reis Ferreira

Este é um trabalho desenvolvido para a disciplina de Fundamentos de Projeto e Análise de Algoritmos, ministrada pelo professor João Paulo Aramuni em 2025/1 no bacharelado em Engenharia de Software da PUC Minas.

Consiste na implementação  do algoritmo A * para encontrar o menor caminho em um labirinto 2D entre dois pontos, evitando obstáculos e considerando os custos dos
movimentos.

O arquivo main.py contém o código com a implementação e o arquivo tests.py contém alguns cenários de teste.

### Regras do Labirinto:
1. O labirinto é representado por uma matriz 2D, onde:
- 0: Células livres (onde o robô pode se mover).
- 1: Obstáculos (onde o robô não pode passar).
- S: Ponto inicial (start).
- E: Ponto final (end).

Exemplo de labirinto:
```
S 0 1 0 0
0 0 1 0 1
0 1 0 0 0
1 0 0 E 1
```

2. O robô pode se mover para as células adjacentes (cima, baixo, esquerda e
direita), desde que a célula não seja um obstáculo ou esteja fora dos limites do
labirinto.


## Como rodar o projeto
1. Clone o repositório do projeto `git clone git@github.com:milenalara/pathfinder.git`
2. Abra o diretório no seu terminal de linha de comando e execute `python main.py` ou `python3 main.py` (à depender da versão do Python instalada na sua máquina).

## Versão do Python
Este projeto foi desenvolvido na versão 3.12.3 do Python.

## Explicação das funções

### heuristica(a, b)
Calcula a distância de Manhattan entre dois pontos a e b.
- Essa é a heurística usada pelo algoritmo A* para estimar a distância até o destino.
- Fórmula: |x1 - x2| + |y1 - y2|

### encontrar_ponto(matriz, ponto)
Percorre a matriz e retorna as coordenadas do ponto desejado (S ou E).
- Serve para localizar onde o robô começa e onde ele precisa chegar.

### vizinhos(pos, matriz)
Retorna uma lista de coordenadas adjacentes válidas (cima, baixo, esquerda, direita) da posição atual.
- Ignora posições com obstáculos (1) ou fora dos limites da matriz.

### a_estrela(matriz)
Implementa o algoritmo A*:
- Usa uma fila de prioridade (heap) para explorar os caminhos.
- Calcula f(n) = g(n) + h(n) para decidir o próximo passo.
- Retorna o menor caminho do início ao fim como uma lista de coordenadas.

### mostrar_caminho(matriz, caminho)
Marca o caminho encontrado no labirinto com *, sem alterar S e E.
- Cria uma cópia da matriz original com o trajeto visualmente destacado.

### imprimir_matriz(matriz)
Imprime a matriz no console, organizando os elementos para fácil leitura.
- Mostra o labirinto original ou o labirinto com o caminho final.

## Exemplo de uso

### Entrada

```
labirinto = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1],
]
```

### Saída
```
Caminho encontrado (coordenadas):
[(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
Labirinto com caminho:
S * 1 0 0
0 * 1 0 1
1 * 1 0 0
1 * * E 1
```