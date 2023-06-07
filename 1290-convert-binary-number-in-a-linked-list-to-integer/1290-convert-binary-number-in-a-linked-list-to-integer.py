# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        dummynode=ListNode()
        dummynode.next=head
        current=dummynode
        listt=[]
        while current:
            current=current.next
            if current!=None:
                value=current.val
                listt.append(value)
        for i in range(len(listt)):
            listt[i]=str(listt[i])
        bitvalue="".join(listt)  
        decimalvalue=int(bitvalue,2)
        return(decimalvalue)
            
            
        