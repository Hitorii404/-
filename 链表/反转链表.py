# https://leetcode.cn/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class MyLinkedListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy_head = MyLinkedListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        p = self.dummy_head
        while index >= 0:
            p = p.next
            index -= 1
        return p.val

    def addAtHead(self, val: int) -> None:
        tmp = MyLinkedListNode(val)
        tmp.next = self.dummy_head.next
        self.dummy_head.next = tmp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        tmp = MyLinkedListNode(val)
        p = self.dummy_head
        while p.next is not None:
            p = p.next
        p.next = tmp
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        tmp = MyLinkedListNode(val)
        p = self.dummy_head
        while index > 0:
            p = p.next
            index -= 1
        tmp.next = p.next
        p.next = tmp
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        p = self.dummy_head
        while index > 0:
            p = p.next
            index -= 1
        tmp = p.next
        p.next = tmp.next
        self.size -= 1
        del tmp

    def printMyLinkedList(self):
        p = self.dummy_head.next
        while p is not None:
            print(p.val, end='->')
            p = p.next
        print('\n', '-' * 50, sep='')


class Solution:
    def reverseList(self, head: Optional[MyLinkedListNode]) -> Optional[MyLinkedListNode]:
        cur = head
        pre = None
        while cur:
            temp = cur.next  # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre  # 反转
            # 更新pre、cur指针
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    myLinkedList = MyLinkedList()
    myLinkedList.addAtTail(1)
    myLinkedList.addAtTail(2)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtTail(4)
    myLinkedList.addAtTail(5)
    myLinkedList.printMyLinkedList()

    s = Solution()
    myLinkedList.dummy_head.next = s.reverseList(myLinkedList.dummy_head.next)
    myLinkedList.printMyLinkedList()
    print(myLinkedList.size)
