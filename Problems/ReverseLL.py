class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = head
        second = first.next
        
        while(second):
            Third = second.next
            second.next = first
            first = second
            second = third
        
        head.next = None
        head = first
        return head
