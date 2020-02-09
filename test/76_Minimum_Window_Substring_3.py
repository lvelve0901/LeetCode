#!/usr/bin/python3
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans = ""
        max_len = len(s)+1

        if len(s) > 0 and len(t) > 0 and len(s) >= len(t):

            counter = collections.Counter(t)
            start, end = 0, 0
            left, right, target = 0, 0, len(t)

            for right in range(len(s)):
                if counter[s[right]] > 0:
                    target -= 1
                counter[s[right]] -= 1

                while target == 0:
                    if not end or end - start >= right - left:
                        start, end = left, right
                    
                    if counter[s[left]] >= 0:
                        target += 1
                    counter[s[left]] += 1
                    left += 1
            
            ans = s[start:end+1]

        return ans

        


def main():

    c = Solution()
    #s = "ADOBECODEBANC"
    #s = "aa"
    s = "cabwefgewcwaefgcf"
    #s = "cabwefgewccccwaefgcf"
    print(s)
    #t = "ABC"
    #t = "aa"
    t = "cae"
    print(t)
    ans = c.minWindow(s,t)
    print(ans)


if __name__ == "__main__":
    main()


