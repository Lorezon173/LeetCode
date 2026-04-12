#
# @lc app=leetcode.cn id=3741 lang=python3
#
# [3741] 三个相等元素之间的最小距离 II
#

# @lc code=start
class Solution:
    def findmini2(self,nums):
        # x,y,z=[0]*3
        diff=[]
        for i in range(1,len(nums)):
            diff.append(nums[i]-nums[i-1])
        interval_min=diff[1]+diff[0]
        for i in range(2,len(diff)):
            if diff[i]+diff[i-1]<interval_min:
                interval_min=diff[i]+diff[i-1]
        return interval_min

    def minimumDistance(self, nums: List[int]) -> int:
        m=len(nums)
        if m<3:
            return -1
        num_dic={}
        for i in range(m):
            if nums[i] not in num_dic:
                num_dic[nums[i]]=[i]
            else:
                num_dic[nums[i]].append(i)
        ans=[]
        flag=False
        for value in num_dic.values():
            if len(value)<3:
                continue
            else:
                flag=True
                interval_min=self.findmini2(value)
                ans.append(2*interval_min)
        if not flag:
            return -1
        return min(ans)

        
# @lc code=end
sol=Solution()
# test= [[1,2,1,1,3], [1,1,2,3,2,1,2],[1,1,2],[1,1,1,1],[2,2,3,2,2]]
test= [[2,2,3,2,2]]
# test2= [1,1,2,3,2,1,2]
for i in range(len(test)):
    print(sol.minimumDistance(test[i]),'\n')
'''
首先需要遍历整个数组，用字典存放同元素下标信息，针对超过三个下标的元素进行进一步处理，
    × 超过三个元素就统计最小的三个下标距离值x,y,z，最小值是min(x+y+z,2*(x+y))
    √ 超过三个元素应该统计的是最小的邻居距离值，直接返回最下的interval_min，该三元组的最小距离应该是2*interval_min
正确思路：
    1、遍历数组，建立字典存放相同元素的下标，dic的内容是nums[i]:[i]，即元素值作为key，value是相同元素的下标列表；
    2、遍历dict中所有的value列表：
        2.1、如果value的长度小于3，说明没达到三元组，跳过
        2.2、如果value的长度大于等于3，达到三元组，计算每个位置的间距数组diff，在diff中找到和最小的近邻位置和interval_min；
    3、将每个value的最小总间隔（2*interval_min）存入ans列表，返回ans中的最小间隔
'''