#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
#Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr=ListNode()
        dummy=curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                print(curr.val)
                curr=curr.next
                print("curr:", curr.val )
                list1 = list1.next
            else:
                curr.next = list2
                print("curr:", curr.val) #this is still 0 in fir
                curr=curr.next
                print(curr.val)
                list2 = list2.next
        curr.next = list1 if list1 else list2
        return dummy.next 
        

list1=ListNode(1,ListNode(2,ListNode(3,ListNode(6))))
list2=ListNode(1,ListNode(2,ListNode(2)))
sol=Solution()
merged=sol.mergeTwoLists(list1,list2)
#print(merged) this is not the way to print a linked list this will only print the obejct reference 

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

print_list(merged)


        

        
# @lc code=end

