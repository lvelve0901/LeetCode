#!/usr/bin/python3

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        ans = 0
        if len(s) > 0 and k > 0:
            if len(s) <= k:
                ans = len(s)
            else:
                
                start,end = 0,0
                left = 0
                target = 0
                sub_dic = {}

                for ss in s:
                    sub_dic[ss] = 0

                for right in range(len(s)):
                    
                    if sub_dic[s[right]] == 0:
                        target += 1
                    sub_dic[s[right]] += 1

                    if target <= k:
                        if right - left > end - start:
                            start,end = left,right

                    print((s[right],left,right,start,end,target,sub_dic))

                    while(target > k):

                        sub_dic[s[left]] -= 1
                        if sub_dic[s[left]] == 0:
                            target -= 1
                        left = left + 1

                ans = end - start + 1

        return ans



def main():

    c = Solution()
    s = "eceba"
    s = "baacccacacabcaabbbbc"
    k = 2

    result = c.lengthOfLongestSubstringKDistinct(s,k)
    print(result)

if __name__ == "__main__":
    main()


