class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        m = {}
        maxlen = 0

        for num in nums:

            lengthLeft = 0
            leftPointer = num - 1
            while leftPointer in m:
                m[leftPointer] += 1
                lengthLeft += 1
                leftPointer -= 1

            lengthRight = 0
            rightPointer = num + 1
            while rightPointer in m:
                m[rightPointer] += 1
                lengthRight += 1
                rightPointer += 1

            m[num] = 1 + lengthRight + lengthLeft
            maxlen = max(maxlen, 1 + lengthRight + lengthLeft)

        return maxlen
            

        