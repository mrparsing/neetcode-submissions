class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Taglia la lista a metà e inverti la seconda parte
        curr = slow.next
        slow.next = None  # <-- FONDAMENTALE: evita il ciclo finale!
        
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 3. Unisci le due metà (intreccio)
        curr1 = head
        curr2 = prev

        # Basta controllare curr2, perché la seconda metà è sempre 
        # uguale o più corta della prima di un nodo.
        while curr2:
            next1 = curr1.next
            next2 = curr2.next

            curr1.next = curr2
            curr2.next = next1

            curr1 = next1
            curr2 = next2