def generate_combinations(nums):
    
    n = len(nums)
    combinations = [[]]

    for i in range(n):
        current_combination = []
        for combination in combinations:
            current_combination.append(combination + [nums[i]])
        combinations += current_combination

    return combinations

def knapsack_exhaustive_search(values, weights, capacity):

    n = len(values)
    max_value = 0

    combinations = generate_combinations(list(range(n)))

    for combo in combinations:
        total_value = sum(values[i] for i in combo)
        total_weight = sum(weights[i] for i in combo)
        if total_weight <= capacity:
            max_value = max(max_value, total_value)
            combination = combo

    return (combination, max_value)

weights = [7,3,4,5]
values = [42,12,40,25]
capacity = 10

comb, price = knapsack_exhaustive_search(values, weights, capacity)
comb = [num+1 for num in comb]
print("Combination: ", comb)
print("Price: ", price)