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