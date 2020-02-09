#!/usr/bin/python3

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ans = ""
        max_len = len(s)+1

        if len(s) > 0 and len(t) > 0 and len(s) >= len(t):

            t_dic = {}
            s_dic = {}
            filtered_S = []

            for tt in t:
                if tt in t_dic:
                    t_dic[tt] += 1
                else:
                    t_dic[tt] = 1
                s_dic[tt] = 0

            for idx, ss in enumerate(s):
                if ss in t_dic:
                    filtered_S.append(idx)

            left = 0

            for right in range(len(filtered_S)):
                
                s_dic[s[filtered_S[right]]] += 1

                contain = True
                for tt in t_dic:
                    if t_dic[tt] > s_dic[tt]:
                        contain = False
                
                if contain is True and max_len > filtered_S[right]-filtered_S[left]+1:
                    max_len = min(max_len,filtered_S[right]-filtered_S[left]+1)
                    ans = s[filtered_S[left]:filtered_S[right]+1]

                while(contain is True):
                    
                    s_dic[s[filtered_S[left]]] -= 1
                    left += 1
                    for tt in t_dic:
                        if t_dic[tt] > s_dic[tt]:
                            contain = False
                    
                    if contain is True and max_len > filtered_S[right]-filtered_S[left]+1:
                        max_len = min(max_len,filtered_S[right]-filtered_S[left]+1)
                        ans = s[filtered_S[left]:filtered_S[right]+1]

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
    print(t)
    ans = c.minWindow(s,t)
    print(ans)


if __name__ == "__main__":
    main()


