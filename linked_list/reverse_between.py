# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


testcase = ListNode(
    val=1,
    next=ListNode(
        val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))
    ),
)

n, m = 2, 4


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if head is None:
            return None

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            temp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = temp

        return root.next


if __name__ == "__main__":
    solution = Solution().reverseBetween(testcase, n, m)
    while solution is not None:
        print(solution.val)
        solution = solution.next
