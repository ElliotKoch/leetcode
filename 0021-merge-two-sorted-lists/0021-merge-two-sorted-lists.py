# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the merged_list
        head_merged_linked_list = ListNode()
        # Create a curr variable to keep track of the head of the merged_linked_list
        curr = head_merged_linked_list
        # Go thourgh each linked lists
        while list1 is not None or list2 is not None:
            # Add the smaller number to the merged_list
            if list1 is None:
                curr.next = list2
                list2 = list2.next
            elif list2 is None:
                curr.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # .next to not take the first val (0) during the initialization
        return head_merged_linked_list.next
           

        