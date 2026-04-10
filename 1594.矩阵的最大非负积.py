#
# @lc app=leetcode.cn id=1594 lang=python3
#
# [1594] 矩阵的最大非负积
#

# @lc code=start
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        maxval=[]
        minval=[]
        MOD=1e9+7
        for _ in range(m):
            temp=[]
            for _ in range(n):
                temp.append(0)
            maxval.append(temp[:])
            minval.append(temp[:])
        nums=1
        for i in range(m):
            nums*=grid[i][0]
            minval[i][0]=nums
            maxval[i][0]=nums
        nums=1
        for j in range(n):
            nums*=grid[0][j]
            minval[0][j]=nums
            maxval[0][j]=nums
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]>=0:
                    maxval[i][j]=max(maxval[i-1][j],maxval[i][j-1])*grid[i][j]
                    minval[i][j]=min(minval[i-1][j],minval[i][j-1])*grid[i][j]
                else:
                    maxval[i][j]=min(minval[i-1][j],minval[i][j-1])*grid[i][j]
                    minval[i][j]=max(maxval[i-1][j],maxval[i][j-1])*grid[i][j]
        
        # print('maxval:\n')
        # for i in range(m):
        #     for j in range(n):
        #         print(f'{maxval[i][j]}\t')
        #     print('\n')
        
        # print('minval:\n')
        # for i in range(m):
        #     for j in range(n):
        #         print(f'{minval[i][j]}\t')
        #     print('\n')

        # if maxval[m-1][n-1]<0:
        #     return -1
        # else:
        #     return maxval[m-1][n-1]
        return int(maxval[m-1][n-1]%MOD) if maxval[m-1][n-1]>=0 else -1

        
# @lc code=end
import sys
for line in sys.stdin:
    m,n=map(int,line.split())
    grid=[]
    for i in range(m):
        in_line=sys.stdin.readline().strip()
        grid.append(list(map(int,in_line.split())))
    sou=Solution()
    sou.maxProductPath(grid)
    print(sou)

"""3 
一、确定dp及其下标含义：
    maxval[i][j]表示从起点到位置(i,j)的所有可能路径中的最大积
    minval[i][j]表示从起点到位置(i,j)的所有可能路径中的最小积
二、确定状态转移方程
    要获得最大非负积，和当前值grid[i][j]有关联，
        1、grid[i][j]>=0,那么最大非负积就是上一情况（(i-1,j)和(i,j-1)）的最大的最大积×grid[i][j]
        2、grid[i][j]<0，那么最大非负积就是上一情况的最小的最小积xgrid[i][j]
        问题的关键在于：如何获取上一情况的最大非负积和最小负积
        if grid[i][j]>=0:
            maxval[i][j]=max(maxval[i-1][j],maxval[i][j-1])*grid[i][j]
            minval[i][j]=min(minval[i-1][j],minval[i][j-1])*grid[i][j]
        else：
            maxval[i][j]=min(minval[i-1][j],minval[i][j-1])*grid[i][j]
            minval[i][j]=max(maxval[i-1][j],maxval[i][j-1])*grid[i][j]
三、确定初始状态
    第一行和第一列有且只有一种方式，因为只能向右或向下走,因此最大积=最小积


"""
