# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        someList = []
        while head:
            someList.append(head.val)
            head = head.next
        
        l = 0
        r = len(someList) - 1
        while l < r and someList[l] == someList[r]:
            l += 1
            r -= 1
        return l >= r