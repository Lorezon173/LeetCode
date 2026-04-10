import sys

class Solution:
    # 加上 self，并将 m, n 作为参数传入
    def bagchoose_2d(self, m, n, rooms, values):
        # dp[i][j] 表示前 i 个物品，放入容量为 j 的背包的最大价值
        dp = [[0 for _ in range(n + 1)] for _ in range(m)]
        
        # 1. 初始化第一行 (仅考虑第 0 个物品)
        for j in range(n + 1):
            if j >= rooms[0]:
                dp[0][j] = values[0]
        
        # 2. 遍历后续物品
        # i 从 1 开始，因为 0 已经初始化过了
        for i in range(1, m):
            # j 必须从 0 遍历到 n
            for j in range(n + 1):
                if j < rooms[i]:
                    # 背包容量不够，装不下当前物品，只能继承上一个状态
                    dp[i][j] = dp[i-1][j]
                else:
                    # 装得下，在“不装”和“装”之间取最大值
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - rooms[i]] + values[i])
                    
        return dp[m-1][n]
    def bagchoose_1d(self,m,n,rooms,values):
        dp=[0]*(n+1)
        for i in range(m):
            for j in range(n,0,-1):
                if j<rooms[i]:
                    dp[j]=dp[j]
                else:
                    dp[j]=max(dp[j],dp[j-rooms[i]]+values[i])
        # #优化：
        # for i in range(m):
        #     for j in range(n,rooms[i],-1):
        #             dp[j]=max(dp[j],dp[j-rooms[i]]+values[i])
        return dp[n]


# 处理 ACM 模式的输入输出
for line in sys.stdin:
    if not line.strip():
        continue
    m, n = map(int, line.strip().split())
    rooms = list(map(int, sys.stdin.readline().split()))
    values = list(map(int, sys.stdin.readline().split()))
    
    sol = Solution()
    # print(sol.bagchoose_2d(m, n, rooms, values))
    print(sol.bagchoose_1d(m, n, rooms, values))

'''
dp[i][j]表示从[0,i-1]个物品任意装入背包后，背包占用j空间的最大价值
dp[j]表示背包占用j空间，背包的最大价值
    dp[j]=max(dp[j],dp[j-weight[i]]+values[i])
'''