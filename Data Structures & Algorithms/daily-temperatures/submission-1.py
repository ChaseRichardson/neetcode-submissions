class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ret = [0] * len(temps)
        st = []

        for i, t in enumerate(temps):
            while st and t > st[-1][0]:
                _, pos = st.pop()
                ret[pos] = i - pos
            
            st.append((t, i))

        return ret







            
