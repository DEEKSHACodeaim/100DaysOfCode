class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #tortoise and rabbit algo

        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            fast=fast.next.next #move fast pointer at twice the speed
            slow = slow.next

        return slow
