def subset_sum(S, d):
    subsets = []

    def backtrack(i, current_sum, current_subset):

        if current_sum == d:
            subsets.append(current_subset[:])
        
        if current_sum > d or i >= len(S):
            return
        
        # Include the current number
        current_subset.append(S[i])
        backtrack(i + 1, current_sum + S[i], current_subset)
        current_subset.pop()
        
        # Exclude the current number
        backtrack(i + 1, current_sum, current_subset)

    backtrack(0, 0, [])
    return subsets


S = [1, 2, 5, 6, 8]
d = 9

result = set(tuple(subset) for subset in subset_sum(S, d))

print("Subsets that sum to the target:")
for subset in result:
    print(subset)
