# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


testcase1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
testcase2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1


if __name__ == "__main__":
    solution = Solution().mergeTwoLists(testcase1, testcase2)
    while solution is not None:
        print(solution.val)
        solution = solution.next
