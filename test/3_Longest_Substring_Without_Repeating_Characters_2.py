#!/usr/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        tmp = 0
        left = 0
        dic = {}

        if len(s) > 0:

            for right in range(len(s)):

                if s[right] in dic and left <= dic[s[right]]:
                    
                    left = dic[s[right]] + 1
                    tmp = right - left + 1
                    dic[s[right]] = right

                else:
                    dic[s[right]] = right
                    tmp = right - left + 1
                    ans = max(ans,tmp)

        return ans


def main():

    c = Solution()
    #s = "abcabcbb"
    #s = "bbbbb"
    #s = ""
    #s = "nfpdmpi"
    s = "pwwkew"
    #s = "tmmzuxt"
    ans = c.lengthOfLongestSubstring(s)

    print(ans)

if __name__ == "__main__":
    main()

