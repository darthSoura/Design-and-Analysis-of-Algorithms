import itertools

def solve_assignment(cost_matrix):
    
    assignments = itertools.permutations(range(len(cost_matrix)))
    
    min_cost = float('inf')
    best_assignment = None

    for assignment in assignments:
        cost = sum([cost_matrix[i][assignment[i]] for i in range(len(cost_matrix))])
        if cost < min_cost:
            min_cost = cost
            best_assignment = assignment

    return best_assignment, min_cost


cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

best_assignment, min_cost = solve_assignment(cost_matrix)
best_assignment = [num+1 for num in best_assignment]
print(f"The best assignment is {best_assignment} with a total cost of {min_cost}.")
