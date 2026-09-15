# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListHelper(head, None)

    def reverseListHelper(self, head: Optional[ListNode], currChain: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return currChain
        print("head", head.val)

        tmp = ListNode(head.val, currChain)
        currChain = tmp
        self.printList(currChain)

        head = head.next

        return self.reverseListHelper(head, currChain)


    def printList(self, head: Optional[ListNode]):
        print("chain: ", end='')
        while head is not None:
            print(head.val, end = '')
            head = head.next