#
# @lc app=leetcode.cn id=2751 lang=python3
#
# [2751] 机器人碰撞
#

# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        sorted_index=sorted(range(len(positions)),key=lambda i:positions[i]
        
# @lc code=end

'''
由于机器人是的位置数组的乱序的，因此需要先排列，而后续仍要按照原位置信息输出，因此需要保留原排列，要建立一个顺序的排列index
'''