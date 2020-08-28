# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


testcase = ListNode(
    val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=None)))
)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        # recursive 

        def reverse(node: ListNode, prev: ListNode=None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)        
        """

        node, prev = head, None

        while node is not None:

            next, node.next = node.next, prev
            prev, node = node, next

        return prev


if __name__ == "__main__":
    solution = Solution().reverseList(testcase)
    while solution is not None:
        print(solution.val)
        solution = solution.next
