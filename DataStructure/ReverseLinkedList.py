class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            # 노드를 순회하면서, next 값은 변경시켜 준다.
            # 가변객체의 .next 값은 해당 값
            next_node, node.next = node.next, prev
            # 변수에 새로운 노드 할당
            prev, node = node, next_node
       return prev