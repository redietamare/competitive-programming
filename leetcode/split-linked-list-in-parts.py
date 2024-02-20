# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr= curr.next
        size = length // k
        add =length % k
        
        prev = None
        curr = head
        ans =[]
        for i in range(k):
            ans.append(curr)
            for j in range(size + (1 if add > 0 else 0)):
                prev = curr
                curr =curr.next
            if prev: 
                prev.next = None
            add-= 1
        
        return ans
    
    
    