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
        currChain = ListNode(head.val, currChain)
        head = head.next
        return self.reverseListHelper(head, currChain)