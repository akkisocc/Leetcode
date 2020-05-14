"""
Steps:
1. Initialize trie class with children [26] and end=False with another class
2. calculate index to know where to store character --> _index()
3. Insert
-- iterate over character of word
-- check with char exist at given index if not insert new Node else ignore
4. Search
-- iterate over char of word
-- check with char exist at given index if not return False , loop exhausts and end is True --> return True
   else False
5. startwith
--iterate over char of word
--check with char exist at given index if not return False, loop exhausts, return True

Time Complexity:
Insertion, Search, startwith = O(len(word))

Space Complexity: O(26*N*len(word))


"""
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()     
        
    def _index(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self, word: str) -> None:
        n = len(word)
        curr = self.root
        for level in range(n):
            char = word[level]
            index = self._index(char)
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end = True
        
            
    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index = self._index(ch)
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        if curr.end == True:
            return True
        return False

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            index = self._index(ch)
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
