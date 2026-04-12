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
            # elif len(value)==3:
            #     flag=True
            #     x,y=[value[i]-value[i-1] for i in range(1,3)][:]
            #     ans.append(2*(x+y))
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
首先需要遍历整个数组，用字典存放同元素下标信息，针对超过三个下标的元素进行进一步处理，超过三个元素就统计最小的三个下标距离值x,y,z，最小值是min(x+y+z,2*(x+y))
'''