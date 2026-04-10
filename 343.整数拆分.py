#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        dp=[]
        for _ in range(n+1):
            dp.append(0)
        # dp[1],dp[2],dp[3]=0,2,3
        # for i in range(4,n+1):
        #     dp[i]=max(dp[i-2]*2,dp[i-3]*3)
        #     # print(dp[i],' ')
        dp[2],dp[3]=1,2
        for i in range(3,n+1):
            for j in range(1,i//2+1):
                dp[i]=max(j*dp[i-j],j*(i-j),dp[i])
        return dp[n]
        
# @lc code=end
sol=Solution()
print(sol.integerBreak(10))
'''
一、确定dp及其下标含义
    dp[i]表示整数i可以拆分得到的最大乘积
二、确定状态转移方程（划分子问题）
    每个i都可以拆分成2+i-2,3+i-3，2+2+i-4,只要将其拆分成多个2和3即可，那么当前i的最大乘积就是i-2的最大乘积x2和i-3的最大乘积x3中选最大的一个
    dp[i]=max(2*dp[i-2],3*dp[i-3])
三、确定初始状态
    n>=2,dp[1]=0,dp[2]=1,dp[3]=2，补dp[1]主要是当i-3=1时，可能存在dp[1]的输出，要么用判断避免，要么直接在初始化时设置为0，这样max后就不会被选择
    此外，定义数组时，需要扩展到n+1,避免dp[n]访问溢出
四、确定遍历顺序
    顺序应该是由小到大，由小的已知到未知
五、打印数组确定

补充：这个方法是存在问题的，无法解释初始化时dp[2]和dp[3]的含义，而且实际上状态转移方程也是有问题的，其实dp[i-2]*2=dp[i-3]*3=max，只适用这道题
以下是重新写的dp过程：
一、确定dp及其下标含义
    dp[i]表示整数i可以拆分得到的最大乘积
二、确定状态转移方程（划分子问题）
    对于每个j(1<=j<i)，dp[i]都可以拆分成j*dp[i-j],因此遍历j，就可以包括所有的组合情况，但是对于i-j很小的情况，如i-j<=3时，dp[i-j]<(i-j)，
        此时取j*(i-j)值更大，此外，在遍历j时，要同时保留当前最大的dp[i]，否则可能在遍历中丢失最大的情况（最大情况一般会在j与i-j最接近时达到），
        进一步来说，我们可以利用这一特性，对代码进行剪枝，仅需将j遍历到i/2处即可（可以等于i/2,因此range的范围应该是(1,i//2+1)，能够将一半的i包含）
    for i in range(3,n+1):
        for j in range(1,i//2+1):
            dp[i]=max(j*dp[i-j],j*(i-j),dp[i])
'''