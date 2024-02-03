class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.end_symbol = '*'

    def suffixTrie(self, string):
        for i in range(len(string)):
            self.insert(i, string)

    def insert(self, index, string):
        node = self.root
        for i in range(index, len(string)):
            letter = string[i]
            if letter not in node.children:
                new_node = TrieNode()
                node.children[letter] = new_node
            node = node.children[letter]
        node.children[self.end_symbol] = None

    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return self.end_symbol in node.children


trie = Trie()
trie.suffixTrie("Nadeem")
print(trie.contains("eem"))
