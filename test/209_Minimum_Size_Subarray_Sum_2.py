#!/usr/bin/python3
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        ans = 0
        if len(nums) > 0:
            tmp_sum = 0
            tmp_ans = len(nums)
            for right in range(len(nums)):
                tmp_sum += nums[right]
                while(tmp_sum >= s and left <= right):
                    tmp_ans = min(tmp_ans,right - left + 1)
                    ans = tmp_ans
                    if ans == 1:
                        break
                    tmp_sum -= nums[left]
                    left += 1
                                
        return ans

def main():

    c = Solution()
    s = 7
    nums = [2,3,1,2,4,3]
    #nums = [7,1,3,4,2,6,2]
    #nums = []
    #nums = [4,2,3,4]

    print(nums)
    result = c.minSubArrayLen(s,nums)
    print(result)

if __name__ == "__main__":
    main()


