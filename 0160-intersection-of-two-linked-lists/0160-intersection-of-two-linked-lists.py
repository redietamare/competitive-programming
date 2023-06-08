# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA=headA
        currentB=headB
        sett=set()
        while currentA:
            sett.add(currentA)
            currentA=currentA.next
        while currentB:
            if currentB in sett:
                intersectval=currentB
                break
            currentB=currentB.next
        return(currentB)
            
        
        
        