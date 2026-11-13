class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numDict = defaultdict(int)
        
        for num in nums:
            numDict[num] += 1


        sortedDict = list(sorted(numDict.items(), key=lambda item: item[1], reverse=True))

        ret = []
        for i in range(k):
            ret.append(sortedDict[i][0])

        return ret

