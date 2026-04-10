#
# @lc app=leetcode.cn id=3418 lang=python3
#
# [3418] 机器人可以获得的最大金币数
#
from typing import List
# @lc code=start
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m,n=len(coins),len(coins[0])
        dp=[[[0 for _ in range(3)] for _ in range(n)] for _ in range(m)]    #size=(m,n,3)
        dp[0][0][0],dp[0][0][1],dp[0][0][2]=coins[0][0],max(coins[0][0],0),max(coins[0][0],0)

        # print('初始列：')
        for i in range(1,m):
            for k in range(3):
                if k==0:
                    dp[i][0][k]=dp[i-1][0][k]+coins[i][0]
                else:
                    dp[i][0][k]=max(dp[i-1][0][k]+coins[i][0],dp[i-1][0][k-1]+max(coins[i][0],0))
                # if k==0:
                #     dp[i][0][k]=dp[i-1][0][k]+coins[i][0]
                # else:
                #     dp[i][0][k]=dp[i-1][0][k-1]
                #     max(dp[i-1][0][k-1],dp[i-1][0][k]-coins[i-1][0])
                # print(f'({i},0,{k}):',dp[i][0][k])
        # print('初始行：')
        for j in range(1,n):
            for k in range(3):
                if k==0:
                    dp[0][j][k]=dp[0][j-1][k]+coins[0][j]
                else:
                    dp[0][j][k]=max(dp[0][j-1][k]+coins[0][j],dp[0][j-1][k-1]+max(0,coins[0][j]))
                # print(f'(0,{j},{k}):',dp[0][j][k])
        for i in range(1,m):
            for j in range(1,n):
                for k in range(3):
                    if k==0:
                        dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k])+coins[i][j]
                    else:
                        dp[i][j][k]=max(dp[i-1][j][k]+coins[i][j],dp[i-1][j][k-1]+max(coins[i][j],0),dp[i][j-1][k]+coins[i][j],dp[i][j-1][k-1]+max(coins[i][j],0))
        
        return dp[m-1][n-1][2]
        


        
        
        
        
    #    ''' temp_sum=0
    #     # print('首列初始化：')
    #     for i in range(1,m):
    #         temp_sum+=coins[i-1][0]
    #         dp[i][0]=temp_sum
    #     #     print(dp[i][0])
    #     # print('首行初始化：')
    #     temp_sum=0
    #     for i in range(1,n):
    #         temp_sum+=coins[0][i-1]
    #         dp[0][i]=temp_sum
    #     #     print(dp[0][i])
    #     skill_list=[]
    #     for i in range(1,m):
    #         for j in range(1,n):
    #             if dp[i-1][j]+coins[i-1][j]>dp[i][j-1]+coins[i][j-1]:
    #                 dp[i][j]=dp[i-1][j]+coins[i-1][j]
    #                 if coins[i-1][j]<0:
    #                      skill_list.append(coins[i-1][j])
    #             else:
    #                 dp[i][j]=dp[i][j-1]+coins[i][j-1]
    #                 if coins[i][j-1]<0:
    #                     skill_list.append(coins[i][j-1])

    #             # if coins[i-1][j]<0 and coins[i][j-1]<0:
                    
    #             #         skill_list.append(coins[i-1][j])
                        
    #             #     elif dp[i-1][j]+coins[i-1][j]==dp[i][j-1]+coins[i][j-1]:
    #             #         if coins[i-1][j]>coins[i][j-1]:
    #             #             skill_list.append(coins[i][j-1])
    #             #             dp[i][j]=dp[i][j-1]+coins[i][j-1]
    #             #         else:
    #             #             skill_list.append(coins[i-1][j])
    #             #             dp[i][j]=dp[i][j-1]+coins[i-1][j]
    #             #     else:
    #             #         skill_list.append(coins[i][j-1])
    #             #         dp[i][j]=dp[i][j-1]+coins[i][j-1]
    #             #     continue
    #             # dp[i][j]=max(dp[i-1][j]+coins[i-1][j],dp[i][j-1]+coins[i][j-1])
        
    #     #使用技能
        
        
        
    #     if coins[m-1][n-1]<0:
    #         skill_list.append(coins[m-1][n-1])
    #     if not len(skill_list):
    #         return dp[m-1][n-1]+coins[m-1][n-1]
    #     skill=0
    #     skill_list.sort()
    #     if len(skill_list)<2:
    #         skill=-sum(skill_list)
    #     else:
    #         skill=-(skill_list[0]+skill_list[1])
    #     return dp[m-1][n-1]+coins[m-1][n-1]+skill'''
        
# @lc code=end
sol=Solution()
print('ans=',sol.maximumAmount([[-16,8,-7,-19],[6,3,-10,13],[13,15,4,-3],[-16,4,19,-12]]))
'''
重复子问题：每次走都依赖于前一个状态
一、确定dp数组及其下标含义：
    含义很清晰，dp[i][j]表示从起点开始，要走到位置(i,j)时，机器人已经获得的最大金币数量，此时还未加上(i,j)获得的金币
二、确定状态转移方程
    先不考虑感化技能：
        到达位置(i,j)都是由(i-1,j)或者(i,j-1)的位置走一步，那么：
            dp[i][j]=max(dp[i-1][j]+coins[i-1][j],dp[i][j-1]+coins[i][j-1])
                那么初值dp[0][0]=0,dp[0][i]=sum(coins[0][:i]),dp[i][0]=sum(coins[:i][0])
    考虑感化技能：
        ❌（贪心策略，此时不适用）初步的想法是，针对每个经过的负数，都进行一个统计，然后将其中的最小的两个负数使用技能，不能全局先用技能，否则
            可能导致机器人不经过使用技能的区域；此外也需要剪枝，仅当下一步的两个都遇到强盗时，才可能触发技能
            if coins[i-1][j]<0 and coins[i][j-1]<0:
                skill_list.append(max(coins[i-1][j],coins[i][j-1]))
            dp[i][j]=max(dp[i-1][j]+coins[i-1][j],dp[i][j-1]+coins[i][j-1])
        ❌修正：统一的策略可能奏效，但是不能遇到两个强盗时才加入判断队列（贪心），可能走负数的那一边后面有更好的数值
            （如向右coins为-1，但是继续向右有coins为100的）
            测试一下全局判断使用技能的情况：只要记录走过的负数即可
            反驳：
                1. 路径选择的“互斥性”：
                你的思路假设你可以先选出一条“金币最多”的路径，然后在这条路径上挑两个负数变零。
                但问题是：如果用了技能，原本“不是最优”的路径可能会变成“最优路径”。
                    举例：路径 A：路过两个 -100 的格子，剩下的全是 +50。
                        路径 B：路过全是 -5 的格子，剩下的全是 +1。
                        如果不准用技能，你肯定选 路径 B（因为扣得少）。如果可以用两次技能，路径 A 才是真正的正确答案（因为-100被抵消后，+50远多于+1）。
                        你的代码会死守着路径 B 走，最后只抵消了两个-5，白白错过了路径 A。
三、确定初值
    dp[0][0]=0,dp[0][i]=sum(coins[0][:i]),dp[i][0]=sum(coins[:i][0])，累加首行首列，
        此外，到达终点时，需要加上终点处的硬币值
四、确定顺序
    顺序从小到大，从左到右

    

正确思路：需要引入第三个维度来记录技能的使用情况，用于记录当前是否使用了技能
一、确定dp数组及其下标含义：
    dp[i][j][k]表示从起点到达(i,j)的位置，使用了k次（k<=2）技能后，机器人获得的总金币数量
二、状态转移方程
    一共是四种情况：从左侧使用技能到达、从左侧不使用技能、从上方使用技能、从上方不使用技能，因此需要对每个位置遍历使用了k次技能后的情况,那么到达(i,j)位置，且使用了k次技能的金币数量为dp[i][j][k]，有以下四种情况：
        1.从左侧来，本次不用技能：dp[i][j-1][k]+coins[i][j]
        2.从左侧来，本次用技能：dp[i][j-1][k-1]+max(coins[i][j],0)
        3.从上侧来，本次不用技能：dp[i-1][j][k]+coins[i][j]
        4.从上侧来，本次用技能：dp[i-1][j][k-1]+max(coins[i][j],0)
            dp[i][j][k]=max(dp[i-1][j][k]+coins[i][j],dp[i-1][j][k-1]+max(coins[i][j],0),dp[i][j-1][k]+coins[i][j],dp[i][j-1][k-1]+max(coins[i][j],0))
    ⭐k的次数需要厘清：主要是看本次是否用技能，本次用就是+max(coins[i][j],0)，且当前是k次技能，所以此时来侧的方向的技能次数应该是k-1,即dp[][][k-1]
三、确定初始状态
    首先需要确定的是，需要初始化首行首列，且每个位置都需要遍历技能的使用情况
    在(0,0)位置，使用一次两次的情况一样



'''