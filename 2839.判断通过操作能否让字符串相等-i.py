#
# @lc app=leetcode.cn id=2839 lang=python3
#
# [2839] 判断通过操作能否让字符串相等 I
#

# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        odd1=sorted([v for i,v in enumerate(s1) if i%2==1])
        odd2=sorted([v for i,v in enumerate(s2) if i%2==1])
        # print(odd1,'\n')
        # print(odd2,'\n')
        if odd1!=odd2:
            return False
        
              
        
        eben1=sorted([v for i,v in enumerate(s1) if i%2==0])
        eben2=sorted([v for i,v in enumerate(s2) if i%2==0])
        # print(eben1,'\n')
        # print(eben2,'\n')
        if eben1!=eben2:
            return False
        return True
        
# @lc code=end


