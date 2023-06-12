# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        current=dummy
        odd=ListNode()
        oddp=odd
        even=ListNode()
        evenp=even
        count=0
        if not head or not head.next:
            return(head)
        while current:
            current=current.next
            count+=1
            if count%2==1:
                oddp.next=current
                oddpoint=oddp
                oddp=oddp.next
            else:
                evenp.next=current
                evenpoint=evenp
                evenp=evenp.next
        if (count-1)%2!=0:
            evenp=evenpoint
        else:
            oddp=oddpoint
        dummy.next=odd.next
        oddp.next=even.next
        return(dummy.next)
            