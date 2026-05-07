class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # naive solution w/ division
        product = 1
        numZeros = 0
        ret = []

        for i in range(len(nums)):

            if nums[i] == 0:
                numZeros += 1
                continue
            
            product *= nums[i]

        if numZeros > 1:
            l = [0] * len(nums)
            return l

        for i in range(len(nums)):

            if numZeros > 0:
                if nums[i] == 0:
                    ret.append(product)

                else:
                    ret.append(0)

            else:
                ret.append(int(product / nums[i]))

        return ret
            
