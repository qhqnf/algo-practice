# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


testcase = ListNode(
    val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=None)))
)


class Solution:
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
            
        return head
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            p = head.next
            head.next = p.next
            p.next = head

            prev.next = p

            head = head.next
            prev = prev.next.next

        return root.next


if __name__ == "__main__":
    solution = Solution().swapPairs(testcase)
    while solution is not None:
        print(solution.val)
        solution = solution.next
