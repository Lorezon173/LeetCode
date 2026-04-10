#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int: 
        if n==1 or n==0:
            return 1
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[0],dp[1],dp[2]=1,1,2
        for i in range(3,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
            # print(dp[i])
        return dp[n]

        
# @lc code=end
sol=Solution()
print(sol.numTrees(3))
'''
重复子问题：以j为根节点时，可能的左子树的结构与以1到j-1为节点构成的二叉搜索树的结构一致；同时右子树也情况相同，
    因此可以考虑dp
一、确定dp及其下标含义;
    dp[i]表示由n个节点最多可以构成的二叉搜索树的数量
二、确定状态转移方程
    如何看状态转移？
    在1<=j<=i，以值j作为根节点，
        左子树的二叉搜索树最大可能数量就是dp[i-1]（左侧是1到i-1的节点构成的二叉搜索树，i-1个）；
        右字数的二叉搜索树最大可能的数量是dp[n-i]（右侧是i+1到n的节点构成的二叉搜索树，n-i个)
    ⭐因此，dp[i]应该是将所有的情况加起来，即将以1，2，3，...,i为根节点可以构成的二叉搜索树的情况加起来
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
三、确定初始值
    无节点时，只有一种可能，空树,dp[0]=1
    一个节点时，只有一种可能,dp[1]=1
    二个节点时，有两种可能,dp[2]=2
四、确定遍历顺序
    从小遍历即可
        
'''