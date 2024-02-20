# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        leftt  = dummy
        rightt = dummy
    
        for i in range(left-1):
            leftt = leftt.next
        for i in range(right):
            rightt = rightt.next
        temp1 = leftt
        leftt = leftt.next
        temp2 = rightt.next
        curr = leftt
        for i in range(left,right+1):
            temp = curr.next
            curr.next = temp2
            temp2 = curr
            curr = temp
        temp1.next = temp2
        return dummy.next