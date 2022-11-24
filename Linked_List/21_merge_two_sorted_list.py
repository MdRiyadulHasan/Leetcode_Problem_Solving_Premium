class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1     
        if l2:
            cur.next = l2
        return dummy.next
if __name__ == '__main__':
    ob1 = ListNode(1)
    ob1.next = ListNode(2)
    ob1.next.next = ListNode(4)
    ob2=ListNode(1)
    ob2.next = ListNode(3)
    ob2.next.next = ListNode(4)
    ob = Solution()
    ans = ob.mergeTwoLists(ob1,ob2)
    tmp = ans
    res = []
    while tmp:
        res.append(tmp.val)
        tmp = tmp.next
    print(res)