#Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using the concept of slow fast pointers
        fast=head
        slow=head
        while  fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow