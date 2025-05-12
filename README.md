# Projeto Path Finder

Implementação do algoritmo A* para encontrar o menor caminho em um labirinto 2D.

Este é um trabalho desenvolvido para a disciplina de Fundamentos de Projeto e Análise de Algoritmos, ministrada pelo professor João Paulo Aramuni em 2025/1 no bacharelado em Engenharia de Software da PUC Minas.

**Alunos:** 
- Guilherme Leroy Teixeira Capanema
- Milena Lara Reis Ferreira

O arquivo main.py contém o código com a implementação e o arquivo tests.py contém alguns cenários de teste.
## Visão Geral

Este projeto consiste na implementação do algoritmo A* (A-estrela) para determinar o menor caminho entre um ponto inicial 'S' e um ponto final 'E' em um labirinto bidimensional. O algoritmo considera obstáculos e os custos dos movimentos (neste caso, custo uniforme para cada passo) para encontrar a rota ótima.

O código principal encontra-se no arquivo `main.py`, e `tests.py` contém cenários para validar a funcionalidade.

## Regras do Labirinto

1.  O labirinto é representado por uma matriz (lista de listas) 2D, onde cada célula pode ser:
    * `0`: Célula livre, por onde o agente pode se mover.
    * `1`: Obstáculo, intransponível pelo agente.
    * `'S'`: Ponto inicial (Start).
    * `'E'`: Ponto final (End).

    **Exemplo de Labirinto:**
    ```
    S 0 1 0 0
    0 0 1 0 1
    0 1 0 0 0
    1 0 0 E 1
    ```

2.  O agente pode se mover para células adjacentes nas quatro direções cardeais (cima, baixo, esquerda, direita), desde que a célula de destino não seja um obstáculo e esteja dentro dos limites do labirinto.

## Como Rodar o Projeto

1.  Clone o repositório do projeto:
    ```bash
    git clone git@github.com:milenalara/pathfinder.git
    ```
2.  Navegue até o diretório do projeto no seu terminal:
    ```bash
    cd pathfinder
    ```
3.  Execute o script principal:
    ```bash
    python main.py
    ```
    (ou `python3 main.py`, dependendo da configuração do seu sistema e versão do Python).

## Versão do Python

Este projeto foi desenvolvido e testado com Python 3.12.3.

## Detalhamento das Funções

### `heuristica(a, b)`

Calcula a distância de Manhattan entre dois pontos `a` e `b` (tuplas `(linha, coluna)`).
Esta função serve como a heurística $h(n)$ no algoritmo A*, estimando o custo do nó atual até o destino.
A fórmula da distância de Manhattan é: $|x_1 - x_2| + |y_1 - y_2|$.

### `encontrar_ponto(matriz, ponto)`

Percorre a `matriz` para localizar e retornar as coordenadas `(linha, coluna)` do `ponto` especificado (seja 'S' para início ou 'E' para fim). Retorna `None` se o ponto não for encontrado.

### `vizinhos(pos, matriz)`

Dada uma posição atual `pos` `(linha, coluna)` e a `matriz` do labirinto, esta função retorna uma lista de todas as coordenadas adjacentes válidas (vizinhas).
São consideradas válidas as células que:
* Estão dentro dos limites da matriz.
* Não são obstáculos (valor `1`).

### `a_estrela(matriz)`

Implementa o algoritmo A* para encontrar o menor caminho.
1.  Localiza os pontos 'S' (início) e 'E' (fim) na `matriz`.
2.  Utiliza uma fila de prioridade (implementada com `heapq`) para gerenciar os nós a serem explorados. A prioridade é determinada pelo custo $f(n)$.
3.  Para cada nó, calcula-se $f(n) = g(n) + h(n)$, onde:
    * $g(n)$: Custo real do caminho desde o nó inicial até o nó atual $n$.
    * $h(n)$: Custo heurístico estimado do nó $n$ até o nó final (calculado por `heuristica`).
4.  Mantém um conjunto de `visitados` para evitar reprocessamento de nós.
5.  Retorna uma lista de tuplas `(linha, coluna)` representando as coordenadas do caminho encontrado, ou uma string indicando "Sem solução" ou erro.

### `mostrar_caminho(matriz, caminho)`

Gera uma nova representação da `matriz` do labirinto com o `caminho` encontrado marcado com asteriscos (`*`). Os pontos 'S' e 'E' são preservados.

### `imprimir_matriz(matriz)`

Imprime a `matriz` (labirinto) no console de forma legível, com cada célula separada por espaços.

## Exemplo de Uso

### Entrada

```python
labirinto = [
    ['S', 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 0, 'E', 1],
]
```

### Saída Esperada no Console

```
Caminho encontrado (coordenadas):
[(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
Labirinto com caminho:
S * 1 0 0
0 * 1 0 1
1 * 1 0 0
1 * * E 1
```
