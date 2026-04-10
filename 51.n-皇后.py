#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List
# @lc code=start
class Solution:

    
    def solveNQueens(self, n: int) -> List[List[str]]:
        #建立棋盘
        # grid=[]
        ans=[]
        grid=[['.'for _ in range(n)] for _ in range(n)]
        # for _ in range(n):
        #     temp=[]
        #     for _ in range(n):
        #         temp.append('.')
        #     grid.append(temp)
        # 创建统计当前已有皇后位置的xy差与xy和，主对角线上坐标差相等，副对角线上坐标和相等
        tilt=[[],[],[]]
        

        def backtracting(x):
            if x==n:
                ans.append([''.join(row) for row in grid])
                return grid
            for j in range(n):
                if (x-j) not in tilt[0] and (x+j) not in tilt[1] and j not in tilt[2]:
                    grid[x][j]='Q'
                    tilt[0].append(x-j)
                    tilt[1].append(x+j)
                    tilt[2].append(j)
                    backtracting(x+1)
                    #状态回退
                    grid[x][j]='.'
                    tilt[0].pop()
                    tilt[1].pop()
                    tilt[2].pop()
        backtracting(0)
        # ans.append(answer)
        
        return ans
            

        
# @lc code=end

sol=Solution()
print(sol.solveNQueens(4))

'''
既然每次会攻击处于同行或同列的棋子，那么在进行遍历放置时，按照行或列放，即放完i行，下次从i+1行开始放，
    当i==n-1时，完成放置，递归自动结束，进行操作回退

'''