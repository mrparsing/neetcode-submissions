# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        write = head
        curr = head.next

        while curr:
            counter = 0
            while curr.val != 0:
                counter += curr.val
                curr = curr.next
            
            write.val = counter
            curr = curr.next
            if curr:
                write = write.next
            else:
                write.next = None
        return head