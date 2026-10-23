# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        distance = []
        index = 1
        while head and head.next and head.next.next:
            prev = head
            curr = head.next
            nextNode = curr.next
            if prev.val > curr.val < nextNode.val or prev.val < curr.val > nextNode.val:
                distance.append(index)
            index += 1
            head = head.next
        if len(distance) < 2:
            return [-1, -1]
        maxDistance = distance[len(distance)-1] - distance[0]
        minDistance = float('inf')
        for i in range(len(distance)-1):
            minDistance = min(minDistance, distance[i+1] - distance[i])
        
        return [minDistance, maxDistance]