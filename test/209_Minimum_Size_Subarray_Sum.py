#!/usr/bin/python3
from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        result = 0
        if len(nums) > 0:

            tmp_sum = nums[0]
            tmp_len = len(nums)
            while(right < len(nums)):
                if tmp_sum < s:
                    #print("left is %d, right is %d, tmp is %d, result is %d, now move right + 1"%(left,right,tmp,result))
                    right += 1
                    if right == len(nums):
                        break
                    else:
                        tmp_sum += nums[right]
                elif tmp_sum >= s:
                    #print("left is %d, right is %d, tmp is %d, result is %d, now move left + 1"%(left,right,tmp,result))
                    tmp_len = min(tmp_len,right-left+1)
                    result = tmp_len
                    if tmp_len == 1:
                        break
                    else:
                        tmp_sum -= nums[left]
                        left += 1

        return result

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


