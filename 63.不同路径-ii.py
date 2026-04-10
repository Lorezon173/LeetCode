#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        # 如果终点有障碍物，那么无法到达
        if obstacleGrid[m-1][n-1]:
            return 0
        if m==n==1:
            return 1
        # 初始化dp数组
        dp=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                if obstacleGrid[i][j]:
                    temp.append(0)
                else:
                    temp.append(1)
            dp.append(temp)
            
        for i in range(m):
            if obstacleGrid[i][0]:
                for k in range(i,m):
                    dp[k][0]=0
        for j in range(n):
            if obstacleGrid[0][j]:
                for k in range(j,n):
                    dp[0][k]=0

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                if obstacleGrid[i][j]:
                    dp[i][j]=0
        return dp[m-1][n-1]

        
# @lc code=end
"""
路径选择问题，选择向右或者向下走，计算路径数量，可以用动态规划
一、确定dp数组及其下标的含义：
    (i,j)表示位置坐标，要求方案数量，因此dp[i][j]表示到(i,j)的方案数量
二、确定状态转移方程：
    到达(i,j)可以由(i-1,j)和(i,j-1)走一步到达，但需要注意去掉障碍物，对应障碍物的格子应直接设定为0
    本质上还是与上一题(62.不同路径-i)一样，dp[i][j]=dp[i-1][j]+dp[i][j-1]
三、确定初始状态
    首先将首行首列初始化，如下会有两种情况：
        1.如果没有障碍物，那么到达的方案仅有一种，全部初始化为1
        2.如果有障碍物，那么障碍物后面的位置将无法到达，设定为0
四、确定遍历顺序
    需要从起点一直走到终点，因此用递增序列即可

"""