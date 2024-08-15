def read_instance(filename):
    with open(filename, 'r') as file:
        n, capacity = map(int, file.readline().strip().split())
        items = []
        for line in file:
            v, w = map(int, line.strip().split())
            items.append((v, w))
    return n, capacity, items

def knapsack_10_instance(filename):
    n, capacity, items = read_instance(filename)
    
    OPT = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        v_i, w_i = items[i - 1]
        for b in range(capacity + 1):
            OPT[i][b] = OPT[i - 1][b]
            for k in range(1, 11):
                if k * w_i <= b:
                    OPT[i][b] = max(OPT[i][b], OPT[i - 1][b - k * w_i] + k * v_i)
    
    b = capacity
    selected_items = []
    for i in range(n, 0, -1):
        v_i, w_i = items[i - 1]
        for k in range(10, 0, -1):
            if b >= k * w_i and OPT[i][b] == OPT[i - 1][b - k * w_i] + k * v_i:
                selected_items.append((i - 1, k))
                b -= k * w_i
                break
    
    optimal_value = OPT[n][capacity]
    print(f"Optimal value: {optimal_value}")
    print("Selected items (item index, quantity):")
    for item in selected_items:
        print(item)

for i in range(1, 9):
    filename = f'inst{i}.txt'
    print(f"Instance {i}:")
    knapsack_10_instance(filename)
    print("\n")
