#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        m=len(stones)
        piv=sum(stones)//2
        dp=[0]*(piv+1)
        #初始化，dp[0]表示容量为0时的最大价值，找最大值，因此初始化为0可以
        for i in range(m):
            for j in range(piv,stones[i]-1,-1):
                dp[j]=max(dp[j],dp[j-stones[i]]+stones[i])
        return sum(stones)-2*dp[piv]
        
# @lc code=end
sol=Solution()
test1=[2,7,4,1,8,1]
test2=[31,26,33,21,40]
print(sol.lastStoneWeightII(stones=test2))
'''
要让剩下的石头最小，那么就要找最接近二分之一总和的组合，转化为0-1背包：
    从stones中找任意组合的石头，尽量装满sum//2的背包
两种写法：dp_2d和dp_1d
    dp_2d[i][j]表示[0,i-1]个物品任意选，背包容量为j空间时，
        ❌1、是否可行（True or false）      --->适合用于能否找到恰好等于target的情况
        ✔️2、价值最大，也即重量最大         --->都适合，当要求恰好等于target时，加一步判断即可
    dp_1d[j]表示物品任意选，背包容量j空间：   
        ✔️1、表示价值，这里价值=重量，因此找到价值/重量最大
        ❌2、表示是否可行
    实际上，此题与416.分割等和子集类似但不同，主要的不同点在于416要求找到等和的子集，要求必须等和，而此题是找到最接近等和的组合状态，因此在写dp时，应该使用“价值=重量”的思路，找到不超过背包重量上限情况下的最大价值（最大重量）的组合
    tips：j一直表示背包的当前容量，即背包的剩余空间是多少
'''