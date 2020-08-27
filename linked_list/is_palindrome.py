from typing import Deque
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


testcase = ListNode(Node(1), Node(2))


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q: Deque = collections.deque()

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True


if __name__ == "__main__":
    solution = Solution().isPalindrome(testcase)
    print(solution)
