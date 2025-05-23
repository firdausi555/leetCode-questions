# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr=sorted(arr)
        i=0
        temp=head
        while i<len(arr) and temp:
            temp.val=arr[i]
            temp=temp.next
            i+=1
        return head
