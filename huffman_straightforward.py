from itertools import permutations

def prefix_free_encoding(symbol_freq):
    
    symbols = list(symbol_freq.keys())
    perms = permutations(symbols)
    
    min_weighted_avg = float('inf')
    best_encoding = {}
    for perm in perms:
        
        encoding = {}
        code = '0'
        # encoding n-1 symbols
        for symbol in perm[:-1]:
            encoding[symbol] = code
            code = '1' + code
        
        encoding[perm[-1]] = code[:-1]
        # final symbol encoding
            
        weighted_avg = sum([symbol_freq[symbol] * len(encoding[symbol]) for symbol in symbols])
        if weighted_avg < min_weighted_avg:
            min_weighted_avg = weighted_avg
            best_encoding = encoding
        
    return best_encoding, min_weighted_avg

symbol_freq = {'A': 0.40, 'B': 0.10, 'C': 0.10, 'D': 0.10, 'E': 0.30}
encoding, weighted_average = prefix_free_encoding(symbol_freq)

encoding = {key: encoding[key] for key in sorted(encoding)}
weighted_average = round(weighted_average, 3)

print("Encoding: ", encoding)
print("Weighted Average: ", weighted_average)
