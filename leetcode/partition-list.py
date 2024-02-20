# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        great = ListNode()
        currless = less
        currgreat = great
        
        while head:
            
            if head.val < x:
                
                currless.next = head
                currless = currless.next
                
            else:
                
                currgreat.next=head
                currgreat = currgreat.next
                
            head = head.next
        currless.next = great.next
        currgreat.next = None
        return less.next