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
        if not head:
            return None

        # 1. Create copy of each node and insert it after original
        curr = head

        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # 2. Set random pointers
        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        # 3. Separate original and copied lists
        curr = head
        copyHead = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copyHead
        