"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldtoNew = {}

        def clone(node):
            if node in oldtoNew:
                return oldtoNew[node]
            
            copy = Node(node.val)
            oldtoNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        
        return clone(node)


        
