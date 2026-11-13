class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numList = set()

        for num in nums:
            if num not in numList:
                numList.add(num)

            else:
                return True

        return False