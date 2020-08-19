"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#https://www.youtube.com/watch?v=bmjAiDsIDas
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        leftnode  = root
        
        while leftnode != None and leftnode.left != None: 
            self.populatelowerlevel(leftnode) 
            leftnode = leftnode.left 
            
        return root
    
    def populatelowerlevel(self, startnode): 
        
        itr = startnode
        while itr != None: 
            itr.left.next = itr.right
            if itr.next != None : 
                itr.right.next = itr.next.left
            itr = itr.next
