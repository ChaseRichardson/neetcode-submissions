class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        l_prod = [1] * n
        r_prod = [1] * n
        ret = [0] * n

        for i in range(1, n):
            l_prod[i] = nums[i - 1] * l_prod[i - 1]

        for i in range(n - 2, -1, -1):
            r_prod[i] = nums[i + 1] * r_prod[i + 1]
            
        for i in range(n):
            ret[i] = l_prod[i] * r_prod[i]

        return ret 