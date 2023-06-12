# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        prev1,prev2=None,None
        while curr1:
            nextcurr1=curr1.next
            curr1.next=prev1
            prev1=curr1
            curr1=nextcurr1
        while curr2:
            nextcurr2=curr2.next
            curr2.next=prev2
            prev2=curr2
            curr2=nextcurr2
        list1=""
        list2=""
        while prev1:
            list1+=str(prev1.val)
            prev1=prev1.next
        while prev2:
            list2+=str(prev2.val)
            prev2=prev2.next
        intlist1=int(list1)
        intlist2=int(list2)
        summ=str(intlist1+intlist2)
        sumlist=list(summ)
        sumlist.reverse()
        dummy1=ListNode(0)
        sumhead=dummy1
        dummy2=ListNode(None)
        for i in range(len(sumlist)):
            dummy2.val=int(sumlist[i])
            dummy1.next=dummy2
            dummy1=dummy1.next
            dummy2=ListNode(None)
        return(sumhead.next)
        
        
            