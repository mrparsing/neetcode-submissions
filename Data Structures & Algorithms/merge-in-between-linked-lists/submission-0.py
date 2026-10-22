# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        node1 = node2 = None
        head1, head2 = list1, list2

        while head1.next:
            if index+1 == a:
                node1 = head1
            elif index == b:
                node2 = head1.next
            head1 = head1.next
            index += 1
        tail = None
        while head2:
            if not head2.next:
                tail = head2
            head2 = head2.next
        node1.next = list2
        tail.next = node2
        return list1