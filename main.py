import os

def knapsack_10(n, B, values, weights):
    #inicializa tabela
    dp = [[[0, [0] * n] for _ in range(B + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(B + 1):
            dp[i][b] = dp[i - 1][b]

            for k in range(1, 11):
                if k * weights[i - 1] <= b:
                    value = dp[i - 1][b - k * weights[i - 1]][0] + k * values[i - 1]
                    if value > dp[i][b][0]:
                        new_selection = dp[i - 1][b - k * weights[i - 1]][1][:]
                        new_selection[i - 1] = k
                        dp[i][b] = [value, new_selection]
                else:
                    break

    return dp[n][B]

def read_instance(file_path):
    with open(file_path, 'r') as f:
        n, B = map(int, f.readline().split())
        values = []
        weights = []
        for _ in range(n):
            v, w = map(int, f.readline().split())
            values.append(v)
            weights.append(w)
    return n, B, values, weights


def solve_instance(file_path):
    result = read_instance(file_path)
    if result is None:
        return
    
    n, B, values, weights = result
    optimal_value, selected_items = knapsack_10(n, B, values, weights)
    print(f"Instância: {file_path}")
    print(f"Valor ótimo: {optimal_value}")
    print(f"Itens selecionados (quantidade): {selected_items}")
    print("----")

# diretorio dos arquivos de instancia
instances_dir = "." 

all_files = os.listdir(instances_dir)

instance_files = [f for f in all_files if f.startswith("inst") and f.endswith(".txt")]

for file in instance_files:
    file_path = os.path.join(instances_dir, file)
    solve_instance(file_path)

# def solve_10knapsack(values, weights, n, B):
#     # Inicializar a matriz DP
#     DP = [[0] * (B + 1) for _ in range(n + 1)]
#     selected = [[[] for _ in range(B + 1)] for _ in range(n + 1)]

#     # Preencher a matriz DP
#     for i in range(1, n + 1):
#         for b in range(B + 1):
#             DP[i][b] = DP[i - 1][b]  # Não incluir o item i
#             selected[i][b] = selected[i - 1][b].copy()
#             for k in range(1, 11):  # Considerar de 0 a 10 unidades do item i
#                 if k * weights[i - 1] <= b:
#                     new_value = k * values[i - 1] + DP[i - 1][b - k * weights[i - 1]]
#                     if new_value > DP[i][b]:
#                         DP[i][b] = new_value
#                         selected[i][b] = selected[i - 1][b - k * weights[i - 1]] + [(i - 1, k)]

#     # Obter os itens selecionados na solução ótima
#     selected_items = []
#     for item, count in selected[n][B]:
#         selected_items.append((item, count))

#     return DP[n][B], selected_items

# # Ler as instâncias dos arquivos .txt
# instance_files = ['inst1.txt', 'inst2.txt', 'inst3.txt', 'inst4.txt', 'inst5.txt', 'inst6.txt', 'inst7.txt', 'inst8.txt']
# for instance_file in instance_files:
#     with open(instance_file, 'r') as f:
#         lines = f.readlines()
#         n, B = map(int, lines[0].split())
#         values = []
#         weights = []
#         for line in lines[1:]:
#             v, w = map(int, line.split())
#             values.append(v)
#             weights.append(w)

#         # Resolver a instância
#         max_value, selected_items = solve_10knapsack(values, weights, n, B)
#         print(f"Instância {instance_file}:")
#         print(f"Valor máximo = {max_value}")
#         print(f"Itens selecionados: {selected_items}")
#         print()