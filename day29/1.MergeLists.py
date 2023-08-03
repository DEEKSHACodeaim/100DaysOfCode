class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l=ListNode()
        head=l
        t1=list1
        t2=list2

        while t1!=None and t2!=None:

            if t2.val > t1.val:
                l.next=t1
                t1=t1.next
                print(l.val,head.val)
                
            else:
                l.next=t2
                t2=t2.next
                print(l.val,head.val)
                
            l=l.next

        if t2!=None:
            l.next=t2
        if t1!=None:
            l.next=t1
        head=head.next
        

        return head
