# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sett = set()
        currlist1 = headA
        currlist2 = headB
        while currlist1:
            sett.add(currlist1)
            currlist1=currlist1.next
        while currlist2:
            if currlist2 in sett:
                break
            currlist2 = currlist2.next
        return currlist2