import math

def num_bits(n):
    return 1 if n == 0 else int(math.log2(n)) + 1


def fixed_length_encoding(freq_dict):
    
    symbols = freq_dict.keys()
    num_symbols = len(symbols)
    max_bits = num_bits(num_symbols - 1)
    
    encoding_dict = {}
    
    for i, symbol in enumerate(symbols):
        binary_str = format(i, '0' + str(max_bits) + 'b')
        encoding_dict[symbol] = binary_str
    
    weighted_average = 0
    for symbol, freq in freq_dict.items():
        encoding_length = len(encoding_dict[symbol])
        weighted_average += freq * encoding_length
        
    return encoding_dict, weighted_average


symbol_freq = {'A': 0.60, 'B': 0.25, 'C': 0.10, 'D': 0.05}
encoding, weighted_average = fixed_length_encoding(symbol_freq)

encoding = {key: encoding[key] for key in sorted(encoding)}
weighted_average = round(weighted_average, 3)

print("Encoding: ", encoding)
print("Weighted Average: ", weighted_average)