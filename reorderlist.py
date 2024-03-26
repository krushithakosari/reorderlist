# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
#step 1: dind the middle of the list
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
#split the list into 2 halves
        second_half=slow.next
        slow.next=None #end of frst ll
#step 2: reverse the second half ofll
        prev=None
        while second_half:
            temp=second_half.next
            second_half.next
            second_half.next=prev
            prev=second_half
            second_half=temp
#prev is head of reversed second half
#merge the frst half and the reversed second half
        first_half=head
        while prev:
            temp1=first_half.next
            temp2=prev.next
            first_half.next=prev
            prev.next=temp1
            first_half=temp1
            prev=temp2
        return head
