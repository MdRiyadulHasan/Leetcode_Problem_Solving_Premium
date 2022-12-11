class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addword(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addword(w)
        rows = len(board)
        cols = len(board[0])
        res = set()
        path = set()

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in path or board[r][c] not in node.children):
                return
            path.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.end:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            path.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,'')
        return list(res)
if __name__ == '__main__':
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    ob = Solution()
    ans = ob.findWords(board,words)
    print(ans)
        