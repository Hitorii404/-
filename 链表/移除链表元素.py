# https://leetcode.cn/problems/remove-linked-list-elements/description/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        f_ptr = head
        l_ptr = dummy_head
        while f_ptr is not None:
            if f_ptr.val == val:
                f_ptr = f_ptr.next
                l_ptr.next = f_ptr
            else:
                f_ptr = f_ptr.next
                l_ptr = l_ptr.next
        return dummy_head.next



