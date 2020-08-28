# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


testcase1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
testcase2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node is not None:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def toList(self, node: ListNode) -> ListNode:
        list: List = []
        while node is not None:
            list.append(node.val)
            node = node.next

        return list

    def toReverseLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        result = int("".join(str(i) for i in a)) + int("".join(str(i) for i in b))

        return self.toReverseLinkedList(str(result))


if __name__ == "__main__":
    solution = Solution().addTwoNumbers(testcase1, testcase2)
    while solution is not None:
        print(solution.val)
        solution = solution.next
