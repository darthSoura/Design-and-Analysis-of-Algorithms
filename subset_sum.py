def generate_subsets(nums):

    n = len(nums)
    subsets = [[]]

    for i in range(n):
        current_subsets = []
        for subset in subsets:
            current_subsets.append(subset + [nums[i]])
        subsets += current_subsets

    return subsets

def subset_sum(nums, target):
    
    ans = []
    subsets = generate_subsets(nums)
    for subset in subsets:
        if sum(subset) == target:
            ans.append(subset)

    return ans

nums = [3, 1, 5, 9, 12]
target = 12
subset = subset_sum(nums, target)
if subset:
    print(f"Subsets of {nums} that sum up to {target} are {subset}.")
else:
    print(f"There is no subset of {nums} that sums up to {target}.")
