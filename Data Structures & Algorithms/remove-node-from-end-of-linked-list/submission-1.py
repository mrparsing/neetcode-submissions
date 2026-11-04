# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #[5,4,2,4] n = 3
        # 1 2 3 4

        curr = head
        lenght = 0
        while curr:
            curr = curr.next
            lenght += 1
        
        pos = lenght - n

        if pos == 0:
            return head.next

        i = 0
        prev = None
        toDelete = head
        while i != pos:
            prev = toDelete
            toDelete = toDelete.next
            i += 1

        if prev:
            prev.next = toDelete.next
    
        return head
        
