class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for s in strs:
            arr = [0] * 26

            for c in s:
                arr[ord(c) - ord('a')] += 1

            anagrams[tuple(arr)].append(s)

        ret = []

        for k, v in anagrams.items():
            ret.append(list(v))

        return ret

        