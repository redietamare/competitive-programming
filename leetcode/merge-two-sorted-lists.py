# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val>list2.val:
                newnode = ListNode()
                newnode.val = list2.val
                curr.next = newnode
                curr = newnode
                list2 = list2.next
            else:
                newnode = ListNode()
                newnode.val = list1.val
                curr.next = newnode
                curr = newnode
                list1 = list1.next
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next