#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==n==1:
            return 1
        dp=[]
        for i in range(m):
            temp=[]
            for j in range(n):
                temp.append(0) 
            dp.append(temp)
              #创建m x n大小的空矩阵
        # dp[0][0]=1
        # dp[0][1]=dp[1][0]=1
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
                # print(f'i={i},j={j},num={dp[i][j]}')
        return dp[m-1][n-1]

        
# @lc code=end

"""
本题的实质是选方案，每次都是当前位置选择向下或者向右走，一共有多少中选择方案，适合dp
dp五部曲：
一、确定dp数组及其下标的含义：
    dp[i][j]表示走到(i,j)位置有dp[i][j]的方案数量
二、确定递推方程：
    (i,j)可以由(i-1,j)位置向右走一步或者(i,j-1)向下走一步到达
    因此方案数dp[i][j]可以由方案数量dp[i-1][j]和方案数dp[i][j-1]组成，因此总方案数是两种情况的和
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
三、确定数组初始值
    初始规模：
        由于(i,j)表示位置，因此规模就是网格的大小:m x n
    初始值设定
        起点是(0,0)，因此走到（0，0）的方案数量是0，dp[0][0]=0
        走到(1,0)的方案数量是1，dp[1][0]=1；同理dp[0][1]=1
        ⭐ 这题需要对首行首列进行初始化，在我们调用状态方程时，实际上没有遍历dp[0][j]和dp[i][0]即首行首列，因此出现了问题
四、确定遍历顺序
    遍历顺序是从小到大，从左上到右下，直到右下角(i,j)

此外：
    对于Python中数组的初始化，需要用循环创建，dp=[[0]*n]*m创建的数组在修改值的时候dp[0][k]=num，会将对应的dp[i][k]都修改为num
    dp[i](i=1,2,...,n)本质上都是复制的引用，不是复制内容，因此修改dp[i]中任何一个元素，都会改变其他对应位置的元素
"""