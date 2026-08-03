"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None : None}
        cur = head
        while cur:
            cpy = Node(cur.val)
            mp[cur] = cpy
            cur = cur.next
        
        cur = head
        while cur:
            cpy = mp[cur]
            cpy.next = mp[cur.next]
            cpy.random = mp[cur.random]
            cur = cur.next
        return mp[head]