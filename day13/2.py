#Remove Nth Node From End of List
#Approach - # two pointers at a distance of n -not simultanious updation at difference n
       
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         if head==None:
           return head
         fast=slow=head
         for i in range(n):
            fast=fast.next
         if fast==None:
            return head.next
        
         while fast.next:
            fast=fast.next
            slow=slow.next
         slow.next=slow.next.next

         return head
            
