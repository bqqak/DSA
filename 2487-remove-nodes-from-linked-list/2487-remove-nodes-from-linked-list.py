# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            while len(stack) > 0 and current.val > stack[-1].val:
                stack.pop()
            stack.append(current)
            current = current.next
        '''
        [5, 2, 13, 3, 8]
        el = 5 -> st = [5] -> el = 2
        el = 2 -> st = [5, 2] -> el = 13
        el = 13 -> 13 > 2 -> st = [5] -> 13 > 5 -> st = [13] -> el = 3
        el = 3 -> st = [13, 3] -> el = 8
        el = 8 -> 8 > 3 -> st = [13] -> st = [13, 8]
        '''
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
        return stack[0]