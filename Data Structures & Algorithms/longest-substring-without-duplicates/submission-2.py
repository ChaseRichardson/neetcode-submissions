class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        long, r = 0, 0
        seqChars = set()

        for i, c in enumerate(s):

            while r < len(s) and s[r] not in seqChars:
                seqChars.add(s[r])
                r += 1
                long = max(long, r - i)

            seqChars.remove(c)

        return long