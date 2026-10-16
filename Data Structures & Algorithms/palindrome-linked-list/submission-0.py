# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1 = head
        list2 = slow

        prev = None
        curr = list2

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        while prev and list1:
            if prev.val != list1.val:
                return False
            prev = prev.next
            list1 = list1.next
        return True