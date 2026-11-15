class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        high = 0
        low = 1
        for pile in piles:
            high = max(high, pile)

        while high > low:

            med = (high + low) // 2

            numHours = 0
            for pile in piles:
                numHours += math.ceil(pile / med)

            if numHours > h:
                low = med + 1
            else:
                high = med


        return low             
                