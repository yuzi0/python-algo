
# Question : Linked List Components
# Result : 2020/10/10 Success
# Link : https://leetcode.com/problems/linked-list-components/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        linked = False
        while head is not None: 
            if head.val in G:
                linked = True
            else:
                if linked == True: count += 1
                linked = False
            head = head.next
        if linked == True: count += 1
        return count