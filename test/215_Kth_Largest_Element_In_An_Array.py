
import sys
import random
from typing import List

class Solution:

    
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left: int, right: int, pivot_index: int) -> int:
            
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            for i in range(left,right):
                if nums[i] >= pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index
        
        def select(left: int, right: int, k: int) -> int:

            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left,right)
            pivot_index = partition(left,right,pivot_index)
            
            if k == pivot_index + 1:
                ans = nums[pivot_index]
            elif k < pivot_index + 1:
                ans = select(left,pivot_index-1,k)
            else:
                ans = select(pivot_index+1,right,k)

            return ans

        ans = select(0,len(nums)-1,k)
        
        return ans


def main():

    c = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    #nums = [3,2,3,1,2,4,5,5,6]
    #k = 4
    #nums = [99,99]
    #k = 1
    result = c.findKthLargest(nums,k)
    print(result)
    

if __name__ == "__main__":
    main()


