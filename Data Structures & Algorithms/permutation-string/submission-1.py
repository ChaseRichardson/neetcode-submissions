class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        a, b = [0] * 26, [0] * 26

        for i in range(len(s1)):
            a[ord(s1[i]) - 97] += 1
            b[ord(s2[i]) - 97] += 1

        for i in range(len(s1), len(s2)):
            if a == b:
                return True
            b[ord(s2[i]) - 97] += 1
            b[ord(s2[i - len(s1)]) - 97] -= 1

        return a == b