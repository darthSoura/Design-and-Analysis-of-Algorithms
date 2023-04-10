
class HuffmanNode:
    def __init__(self, freq, symbol = None):
        self.freq = freq
        self.symbol = symbol
        self.left = None
        self.right = None
        self.depth = 0
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HuffmanNode):
            return False
        return self.freq == other.freq
    
    def __str__(self):
        if self.symbol is not None:
            return f'Symbol = {self.symbol}, Frequency Sum = {round(self.freq, 3)}'
        else:
            return f'Frequency Sum = {round(self.freq, 3)}'
    
    def print_tree(self, prefix=''):
        if self is None:
            return
        print(prefix + str(self))
        if self.left is not None:
            self.left.print_tree(prefix + '/-- ')
        if self.right is not None:
            self.right.print_tree(prefix + '\-- ')

def argmin(F, T=None):
     
    if T == None:
        minVal = F[0].freq
        smallest = F[0]
        for node in F[1:]:
            if node.freq < minVal:
                smallest = node
                minVal = node.freq
    else:
        if T == F[0]:
            F = F[1:]
        minVal = F[0].freq
        smallest = F[0]
        for node in F[1:]:
            if node != T and node.freq < minVal:
                smallest = node
                minVal = node.freq
                
    return smallest
    
def huffman_straightforward(symbol_freq):
    
    symbols = list(symbol_freq.keys())
    F = []
    for symbol in symbols:
        Ta = HuffmanNode(symbol_freq[symbol], symbol)
        F.append(Ta)
    
    while len(F) > 1:
        
        T1 = argmin(F)
        T2 = argmin(F, T1)
        
        F.remove(T1)
        F.remove(T2)
        
        node_freq = T1.freq + T2.freq
        T3 = HuffmanNode(node_freq)
        T3.left = T1
        T3.right = T2
        T3.depth = max(T1.depth, T2.depth) + 1
        
        F.append(T3)
    
    tree = F[0]
    encoding_table = {}
    if tree:
        root = tree
        traverse_huffman_tree(root, encoding_table)
        
    weighted_average = 0
    for symbol, freq in symbol_freq.items():
        encoding_length = len(encoding_table[symbol])
        weighted_average += freq * encoding_length
    
    return tree, encoding_table, weighted_average

def traverse_huffman_tree(node, encoding_table, encoding=''):
    if node.symbol is not None:
        encoding_table[node.symbol] = encoding
        return
    if node.left is not None:
        traverse_huffman_tree(node.left, encoding_table, encoding + '1')
    if node.right is not None:
        traverse_huffman_tree(node.right, encoding_table, encoding + '0')
        
freq_dict = {'A': 0.60, 'B': 0.25, 'C': 0.10, 'D': 0.05}
tree, encoding, weighted_average = huffman_straightforward(freq_dict)

encoding = {key: encoding[key] for key in sorted(encoding)}
weighted_average = round(weighted_average, 3)

print("Tree:")
tree.print_tree()
print("\nEncoding: ", encoding)  
print("Weighted Average: ", weighted_average)
