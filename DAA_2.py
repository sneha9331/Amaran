import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def preOrder(root, code, codes):
    if root is None:
        return
    if root.left is None and root.right is None:
        codes[root.char] = code
        return
    preOrder(root.left, code + '0', codes)
    preOrder(root.right, code + '1', codes)

def huffmanCodes(chars, freq):
    heap = []
    for i in range(len(chars)):
        heapq.heappush(heap, Node(chars[i], freq[i]))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        newNode = Node(None, left.freq + right.freq)
        newNode.left = left
        newNode.right = right
        heapq.heappush(heap, newNode)
    root = heapq.heappop(heap)
    codes = {}
    preOrder(root, "", codes)
    return codes

def main():
    n = int(input("Enter number of characters: "))
    chars = []
    freq = []
    print("\nEnter characters and their frequencies:")
    for i in range(n):
        ch = input(f"Character {i+1}: ")
        f = int(input(f"Frequency of '{ch}': "))
        chars.append(ch)
        freq.append(f)
    codes = huffmanCodes(chars, freq)
    print("\nHuffman Codes:")
    print("-----------------------")
    for ch in chars:
        print(f"{ch}: {codes[ch]}")

main()
