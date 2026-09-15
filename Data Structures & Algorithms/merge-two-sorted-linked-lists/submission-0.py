# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
   
        dummy = ListNode()

        dummy.next = list1

        list1 = dummy

        while list2 != None:

            #check to make sure list1 still exists
            if list1.next == None:
                list1.next = list2
                break

            if list1.next.val > list2.val:
                tmp = list1.next
                list1.next = ListNode(list2.val)
                list1.next.next = tmp
                list2 = list2.next
                
            list1 = list1.next

        return dummy.next
