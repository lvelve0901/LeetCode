#!/usr/bin/python3

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans = ""
        max_len = len(s)+1

        if len(s) > 0 and len(t) > 0 and len(s) >= len(t):

            left = 0
            tmp = ""
            t_dic = {}
            s_dic = {}

            for d in t:
                if d in t_dic:
                    t_dic[d] += 1
                else:
                    t_dic[d] = 1


            for right in range(len(s)):
                
                tmp = tmp+s[right]

                if s[right] in s_dic:
                    s_dic[s[right]] += 1
                else:
                    s_dic[s[right]] = 1

                isContainAll = True
                for d in t_dic:
                    if d not in s_dic or t_dic[d] > s_dic[d]: 
                        isContainAll = False
                
                if isContainAll == False:
                    print("not contain left=%d right=%d tmp=%s"%(left,right,tmp))

                while(isContainAll == True and left <= right):
                    print("contain left=%d right=%d tmp=%s"%(left,right,tmp))
                
                    if right - left + 1 <= max_len:
                        ans = tmp
                        max_len = right - left + 1
                    
                    s_dic[tmp[0]] -= 1
                    tmp = tmp[1:]
                    left += 1
                    for d in t_dic:
                        if d not in s_dic or t_dic[d] > s_dic[d]: 
                            isContainAll = False

        return ans

        


def main():

    c = Solution()
    #s = "ADOBECODEBANC"
    #s = "aa"
    s = "cabwefgewcwaefgcf"
    print(s)
    #t = "ABC"
    #t = "aa"
    t = "cae"
    ans = c.minWindow(s,t)
    print(ans)


if __name__ == "__main__":
    main()


