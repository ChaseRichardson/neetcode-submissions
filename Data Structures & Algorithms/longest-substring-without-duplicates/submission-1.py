class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        l = 0
        char_set = set()
        ret = 0

        for r in range(len(s)):

            # check to see if r is a dup or not
            if s[r] in char_set:
                
                # move slider untill all unique chars in set
                while s[r] in char_set:

                    char_set.remove(s[l])
                    l += 1

                # at this point we should have all unique chars in set
                # shouldnt need to play with count since its guarantee
                # to be lower then max at this point


                # update ret before counter because we don't know what we add
            char_set.add(s[r])
            ret = max(ret, r - l + 1)

        return ret

            


            

