from queue import PriorityQueue

class HuffmanNode:
    def __init__(self, freq, symbol=None):
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

def huffman_queues(symbol_freq):
    
    symbols = list(symbol_freq.keys())
    F1 = PriorityQueue()
    F2 = PriorityQueue()
    for symbol in symbols:
        Ta = HuffmanNode(symbol_freq[symbol], symbol)
        F1.put(Ta)
    
    while F1.qsize() + F2.qsize() > 1:
        
        if F1.qsize() == 0:
            T1 = F2.get()
        elif F2.qsize() == 0:
            T1 = F1.get()
        else:
            T1 = min(F1.queue + F2.queue)
            if F1.queue[0] == T1:
                T1 = F1.get()
            else:
                T1 = F2.get()
        
        if F1.qsize() == 0:
            T2 = F2.get()
        elif F2.qsize() == 0:
            T2 = F1.get()
        else:
            T2 = min(F1.queue + F2.queue)
            if F1.queue[0] == T2:
                T2 = F1.get()
            else:
                T2 = F2.get()
        
        node_freq = T1.freq + T2.freq
        T3 = HuffmanNode(node_freq)
        T3.left = T1
        T3.right = T2
        T3.depth = max(T1.depth, T2.depth) + 1
        
        F2.put(T3)
    
    tree = F2.get()
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
tree, encoding, weighted_average = huffman_queues(freq_dict)

encoding = {key: encoding[key] for key in sorted(encoding)}
weighted_average = round(weighted_average, 3)

print("Tree:")
tree.print_tree()
print("\nEncoding: ", encoding)  
print("Weighted Average: ", weighted_average)
