class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current=dummy
        while list1 and list2:
            if list1.val<list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current=current.next
        if list1:
            current.next = list1
        if list2:
            current.next =list2
        return dummy.next
list1 = [1,2,4]
list2 = [1,3,4]
ob= Solution()
print(ob.mergeTwoLists(list1,list2))
        
