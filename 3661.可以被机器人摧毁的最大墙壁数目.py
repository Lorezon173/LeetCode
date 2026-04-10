#
# @lc app=leetcode.cn id=3661 lang=python3
#
# [3661] 可以被机器人摧毁的最大墙壁数目
#

# @lc code=start
class treeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
        def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
             
        
# @lc code=end

'''
暴力解题思路：建树，节点为当前robot已经击破的墙数，左子树是向左发射后的robot，右子树是向右发射，
'''