class ListNode:
    def __init__(self,val = 0):
        self.val = val
        self.next = None 
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.dummy = ListNode()
        self.dummy.next = self.head

    def get(self, index: int) -> int:
        curr = self.dummy
        for i in range(index+1):
            curr = curr.next
            if not curr:
                return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
       
        newnode = ListNode(val)
        temp=self.dummy.next
        newnode.next=temp
        self.dummy.next=newnode
    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        newnode = ListNode(val)
        while curr.next:
            curr = curr.next
        
        curr.next = newnode
       
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy
        newnode = ListNode(val)
        for i in range(index):
            curr = curr.next
            if not curr :
                return
        temp = curr.next
        curr.next = newnode
        newnode.next = temp
        # while curr:
        #     if ind == index - 1:
        #         newnode = ListNode(val)
        #         newnode.next=curr.next
        #         curr.next=newnode
        #     ind += 1
        #     curr = curr.next
    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy
        for i in range(index):
            curr = curr.next
            if not curr:
                return
        if not curr.next:
            return
        curr.next = curr.next.next
        
        
            
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)