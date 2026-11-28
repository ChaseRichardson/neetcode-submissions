class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for _ in range(len(nums) + 1)]
        c = Counter(nums)
        ret = []

        for num, count in c.items():
            bucket[count].append(num)

        for item in reversed(bucket):

            for num in item:
                ret.append(num)

            if len(ret) >= k:
                return ret


        return ret




