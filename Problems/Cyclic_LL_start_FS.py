class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def find_cycle_length(self, head: Optional[ListNode]) -> int:
        """
        Helper function to detect the cycle and return its length (K).
        Returns 0 if no cycle is found.
        """
        slow = head
        fast = head
        
        # 1. Find the meeting point (detect cycle)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected. Now calculate length.
                current = slow.next
                cycle_length = 1
                
                # 2. Count nodes until we meet the slow pointer again
                while current != slow:
                    current = current.next
                    cycle_length += 1
                return cycle_length
        
        # If the loop finishes without meeting, there is no cycle
        return 0

    def findCycleStart(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the starting node of a cycle in a singly linked list.

        Args:
            head: The head node of the linked list.

        Returns:
            The starting node of the cycle, or None if no cycle exists.
        """
        # 1. Determine the length of the cycle (K)
        K = self.find_cycle_length(head)
        
        # If K is 0, no cycle exists, so return None.
        if K == 0:
            return None
            
        # 2. Initialize two pointers starting at the head
        pointer1 = head
        pointer2 = head
        
        # 3. Move pointer2 ahead by K nodes (the cycle length)
        for _ in range(K):
            if pointer2 is None:
                # Should not happen if cycle length K > 0 and the list is structured correctly,
                # but this check ensures safety.
                return None 
            pointer2 = pointer2.next
            
        # 4. Move both pointers one step at a time until they meet
        # Since pointer2 is K steps ahead, the meeting point will be the cycle start.
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        # The meeting point is the start of the cycle
        return pointer1
