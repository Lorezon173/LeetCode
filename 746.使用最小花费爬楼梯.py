#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost)
        dp=[0]*(len(cost)+1)
        dp[1]=0
        dp[2]=min(cost[0],cost[1])
        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
            # print(dp[i])

        return dp[len(cost)]
        
        
# @lc code=end

"""
dp五步法：
1、确定dp数组及其下标的含义：
    dp[i]表示走到第i个位置所需要的总花费
2、确定递推公式：
    每次可以有两种走法，走一步或者走两步，那么到达位置i就有i-1和i-2两种走法，那么开销也一样，
    dp[i]=dp[i-1]+cost[i-1] 或者 dp[i]=dp[i-2]+cost[i-2],因此要花费最低，应该找两个方案中开销最小的
        递推公式：dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
3、dp数组的初始化：
    起点信息：
        有两个起点，下标0和下标1的位置，
            a.走到第1个位置有两种方式：
                *从位置0走到1，开销是cost[0];
                *从下标1走到下标1,无开销;
                因此dp[1]=min(0,cost[0])=0
            b.走到第2个位置有两种可能性：
                a)从下标0的位置走两步，开销是cost[0]
                b)从下标1开始走1步，开销是cost[1]
                    dp[2]=min(cost[0],cost[1])
    长度信息：
        由于i表示到达的位置，而题目的楼顶是超过cost数组最大下标n-1的，因此楼顶就是下标n，于是dp[n]需要有效，那么长度就是n+1
4、确定遍历顺序：
    起点是0或1，且当前开销依赖上一状态的开销，因此从左往右
5、打印结果检查
    dp[0]=0,dp[1]=cost[0],dp[2]=min(cost[0],cost[1]),dp[3]=min(dp[1]+cost[1],dp[2]+cost[2])

"""