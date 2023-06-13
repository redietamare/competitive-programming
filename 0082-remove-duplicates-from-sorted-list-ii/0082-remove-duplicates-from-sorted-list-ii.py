# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        current=dummy
        while current and current.next and current.next.next:
            if current.next.val==current.next.next.val:
                x=current.next.val
                while current.next and x==current.next.val:
                    current.next=current.next.next
            else:
                current=current.next
        return(dummy.next)
            