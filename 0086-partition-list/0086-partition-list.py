# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left=ListNode()
        leftpointer=left
        right=ListNode()
        rightpointer=right
        current=head
        while current:
            if current.val<x:
                leftpointer.next=current
                leftpointer=leftpointer.next
            else:
                rightpointer.next=current
                rightpointer=rightpointer.next
            current=current.next
        leftpointer.next=None
        rightpointer.next=None
        leftpointer.next=right.next
        return(left.next)