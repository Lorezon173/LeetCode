#
# @lc app=leetcode.cn id=2840 lang=python3
#
# [2840] 判断通过操作能否让字符串相等 II
#

# @lc code=start
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd1,odd2,eben1,eben2=[],[],[],[]
        for i,v in enumerate(s1):
            if i%2==1:
                odd1.append(v)
            else:
                eben1.append(v)
        odd1.sort()
        eben1.sort()

        for i,v in enumerate(s2):
            if i%2==1:
                odd2.append(v)
            else:
                eben2.append(v)
        odd2.sort()
        eben2.sort()


        if odd1!=odd2 or eben1!=eben2:
            return False
        else:
            return True
# @lc code=end

