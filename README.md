
1. Casos base:
   - OPT(0, b) = 0, para todo b ≥ 0 (nenhum item disponível)
   - OPT(i, 0) = 0, para todo i ≥ 0 (sem capacidade na mochila)

2. Caso geral:
   Para cada k, temos:
   - Se k * w_i > b, não podemos escolher k unidades do item i
   - Se k * w_i ≤ b, podemos escolher k unidades do item i, obtendo um valor k * v_i e deixando uma capacidade de b - k * w_i para os itens anteriores (1 a i-1).

Portanto, a equação de recorrência para OPT(i, b) pode ser expressa da seguinte forma:

OPT(i, b) = max{OPT(i-1, b - k * w_i) + k * v_i | 0 ≤ k ≤ 10, k * w_i ≤ b}

- OPT(i-1, b - k * w_i) representa o valor ótimo considerando os itens de 1 a i-1 com a capacidade residual b - k * w_i.

- k * v_i é o valor obtido ao selecionar k unidades do item i.

A condição k * w_i ≤ b garante que não excedemos a capacidade da mochila.

