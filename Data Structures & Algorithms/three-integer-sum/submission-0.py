class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sNums = sorted(nums)
        pairs = set()

        for i in range(len(sNums) - 2):
            l, r = i + 1, len(sNums) - 1

            while l < r:
                tSum = sNums[i] + sNums[l] + sNums[r]

                if tSum == 0:
                    pairs.add((sNums[i], sNums[l], sNums[r]))
                    l += 1
                    r -= 1
                elif tSum > 0:
                    r -= 1
                else:
                    l += 1
            
        ret = []
        for pair in pairs:
            ret.append(list(pair))

        return ret

                

                
