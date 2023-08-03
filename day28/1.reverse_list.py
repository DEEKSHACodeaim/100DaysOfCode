class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next == None:
            return head
        
        prev=None
        curr=head
        later=curr.next

        while later!= None:

            curr.next = prev

            prev = curr
            curr = later
            later = curr.next
            
        curr.next = prev
        head=curr
        

        return head


