
# Projeto: Problema da Mochila com Capacidade de até 10 Itens por Tipo

Este projeto implementa um algoritmo para o problema da mochila, onde cada tipo de item pode ser selecionado até 10 vezes. A solução utiliza programação dinâmica para determinar a seleção de itens que maximiza o valor total sem exceder a capacidade da mochila.

## Estrutura do Projeto

### Funções Principais

1. **read_instance(filename)**:
   - Lê uma instância do problema a partir de um arquivo.
   - Retorna o número de itens, a capacidade da mochila e uma lista de tuplas (valor, peso) de cada item.

2. **knapsack_10_instance(filename)**:
   - Resolve uma instância do problema da mochila com a restrição de até 10 itens por tipo.
   - Utiliza programação dinâmica para preencher a tabela de soluções ótimas (OPT).
   - Identifica e retorna os itens selecionados na solução ótima.

## Procedimentos

### Leitura da Instância

A função `read_instance(filename)` lê uma instância do problema a partir de um arquivo de texto formatado da seguinte maneira:

- A primeira linha contém dois inteiros, `n` (número de itens) e `capacity` (capacidade da mochila).
- Cada linha subsequente contém dois inteiros, `v` (valor do item) e `w` (peso do item).

### Solução do Problema

A função `knapsack_10_instance(filename)` realiza os seguintes passos:

1. Lê a instância do problema usando `read_instance`.
2. Inicializa a tabela de programação dinâmica `OPT` com dimensões `(n+1) x (capacity+1)`.
3. Preenche a tabela `OPT` considerando a inclusão de até 10 unidades de cada item.
4. Traça a solução ótima para identificar quais itens foram selecionados e em quais quantidades.
5. Imprime o valor ótimo e a lista de itens selecionados.

### Exemplo de Uso

Para testar a função com as instâncias fornecidas (`inst1.txt` a `inst8.txt`):

```python
for i in range(1, 9):
    filename = f'inst{i}.txt'
    print(f"Instance {i}:")
    knapsack_10_instance(filename)
    print("\n")
```
Resultados
Valor Ótimo: O valor total dos itens selecionados que maximiza a capacidade da mochila.
Itens Selecionados: A lista de itens incluídos na solução ótima, representados pelo índice do item e a quantidade selecionada.

Arquivos de Instância
Os arquivos de instância devem estar no seguinte formato:
```python
n capacity
v1 w1
v2 w2
...
vn wn
```

