class TrieNode:
    # We create a trie node class
    def __init__(self):
        self.children = {}
        self.endofword = False

    # define addWord
    # Takes a normal string and converts it to a chain of connected trie
    # nodes
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create an empty starting node
        root = TrieNode()
        # every word in word is converted into a trie
        for w in words:
            root.addWord(w)
        
        # we obtain the dimensions of the grid
        rows, columns = len(board), len(board[0])

        # initialise a set() res to store the words we have found
        # initialse a set() visit to store board positions being used in
        # one DFS path
        res, visit = set(), set()

        # create a dfs function to 
        # takes in the current row, current column, current Trie node
        # current letters collected so far
        def dfs(r, c, node, word):
            # the first if statement if for our base case
            # checks whether continuing from the current cell is invalid
            # r < 0 or c < 0: outside top or left of board
            # r == rows or c == columns: outside bottom or right of board
            # because if there 9 rows valid rows will be from 0-8
            # (r, c) in visit: the cell is already in current path so
            # so the same cell cannot be re-used
            # board[r][c] not in node.children: we know the path won't
            # yield a valid word so we can discard it
            # this is the main optimisation of trie!
            if (r < 0 or c < 0 or 
                r == rows or c == columns or 
                (r, c) in visit or 
                board[r][c] not in node.children):
                return 
            
            # we mark the current cell we are on as used
            # by adding it to our path
            visit.add((r, c))
            # expand path
            node = node.children[board[r][c]]
            # add the letter to word
            word += board[r][c]
            if node.endofword:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(columns):
                dfs(r, c, root, "")

        return list(res) 

        