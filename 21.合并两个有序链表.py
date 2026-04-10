#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_node=ListNode()
        curr=head_node
        p,q=list1,list2
        while p and q:
            if p.val>q.val:
                curr.next=q
                q=q.next
            else:
                curr.next=p
                p=p.next
            curr=curr.next
        if p:
            curr.next=p
        else:
            curr.next=q
        return head_node.next
            

        
# @lc code=end

