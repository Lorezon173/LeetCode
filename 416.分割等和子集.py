#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return False
        totle=sum(nums)
        m=len(nums)
        if totle%2!=0:
            return False
        target=totle//2
        # dp=[[False] *(target+1) for _ in range(m)]
        # dp[0][0]=True
        # for i in range(m):
        #     dp[i][0]=True
        # if nums[0]<target:
        #     dp[0][nums[0]]=True
        # for i in range(1,m):
        #     for j in range(1,target+1):
        #         if j<nums[i]:
        #             dp[i][j]=dp[i-1][j]
        #         else:
        #             dp[i][j]=dp[i-1][j-nums[i]] or dp[i-1][j]

        # return dp[m-1][target]

        dp_1d=[False]*(target+1)
        dp_1d[0]=True
        if nums[0]<=target:
            dp_1d[nums[0]]=True
        for i in range(1,m):
            for j in range(target,nums[i]-1,-1):
                dp_1d[j]=dp_1d[j] or dp_1d[j-nums[i]]
        return dp_1d[target]
# @lc code=end

'''
首先需要知道所有数组的总和，然后判断是否有一个子数组满足和为sum/2，那么问题转化为从数组中找到满足和为sum/2的子数组，类似于已知容量的背包，判断能否找到正好装满背包的物品，每种物品只能取一次
定义dp数组：
    dp[i][j]表示[0,i-1]个数字中任意选数字，已有的数字和为j，是否可行，可行的值为True，否则为false
'''