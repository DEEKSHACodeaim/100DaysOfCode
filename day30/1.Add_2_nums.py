# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        

        l=ListNode()
        head=l
        carry=0
        while l1 and l2:
            temp=ListNode()
            l.next=temp
            sum=l1.val+l2.val+carry
            
            if sum>= 10:
                sum=sum%10
                carry=1
            else:
                carry=0
            temp.val=sum

            l1=l1.next
            l2=l2.next
            l=l.next
        
        #if there is carry from the previous sums need to carry that
        while l1 :
                temp=ListNode()
                l.next=temp
                sum=l1.val+carry
                
                if sum>= 10:
                    sum=sum%10
                    carry=1
                else:
                    carry=0
                temp.val=sum

                l1=l1.next
                l=l.next
            
        while l2 :
                temp=ListNode()
                l.next=temp
                sum=l2.val+carry
                
                if sum>= 10:
                    sum=sum%10
                    carry=1
                else:
                    carry=0
                temp.val=sum

                l2=l2.next
                l=l.next
        if carry==1:
                temp=ListNode()
                l.next=temp
                temp.val= carry
                l=l.next    
        

        
        return head.next


            
