# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        slow=head
        fast=head
        while fast and fast.next:
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        print(stack)
        
        maxSum=0
        while slow:
            maxSum=max(maxSum,stack.pop()+slow.val)
            slow=slow.next
        return maxSum
