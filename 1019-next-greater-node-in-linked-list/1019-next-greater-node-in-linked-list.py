# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        numbers = []
        stack = []
        current = head
        
        while current:
            numbers.append(current.val)
            current = current.next
    
        ans = [0] * len(numbers)
        for i in range(len(numbers)):
            while len(stack) > 0 and numbers[i] > numbers[stack[-1]]:
                ans[stack.pop()] = numbers[i]
            
            stack.append(i)
        return ans