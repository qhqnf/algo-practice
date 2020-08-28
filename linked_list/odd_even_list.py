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


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head


if __name__ == "__main__":
    solution = Solution().oddEvenList(testcase)
    while solution is not None:
        print(solution.val)
        solution = solution.next
