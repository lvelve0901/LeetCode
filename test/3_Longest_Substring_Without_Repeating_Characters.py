#!/usr/bin/python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        if len(s) > 0:
            left = 0
            
            tmp_list = []

            for right in range(len(s)):
                if s[right] not in tmp_list:
                    tmp_list.append(s[right])
                    ans = max(ans,len(tmp_list))
                else:
                    while(s[right] in tmp_list):
                        left_value = s[left]
                        tmp_list = tmp_list[1:]
                        left += 1
                    tmp_list.append(s[right])
                    
        return ans


def main():

    c = Solution()
    #s = "abcabcbb"
    #s = "bbbbb"
    #s = ""
    s = "nfpdmpi"
    ans = c.lengthOfLongestSubstring(s)

    print(ans)

if __name__ == "__main__":
    main()

