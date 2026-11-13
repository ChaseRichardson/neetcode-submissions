class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]

        d = defaultdict(int)
        # counting:
        for num in nums:
            d[num] += 1

        for num, freq in d.items():
            buckets[freq].append(num)

        ret = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ret.append(num)

                if len(ret) >= k:
                    return ret

        return ret




