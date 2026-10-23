from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None
            
            for _ in range(level_size):
                curr = queue.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            prev.next = None

        return root