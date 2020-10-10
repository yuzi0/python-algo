# Question : Copy List with Random Pointer
# Result : 2020/10/10 Success
# Link : https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy1 = copy.deepcopy(head)
        return copy1