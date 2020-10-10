# Question : Reverse Linked List
# Status : 2020/10/10 Success
# Link : https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse: ListNode = None
        
        while head is not None:
            reverse = ListNode(head.val, reverse)
            head = head.next
        return reverse