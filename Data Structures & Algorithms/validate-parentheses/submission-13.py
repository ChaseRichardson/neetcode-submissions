class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {']': '[', '}': '{', ')': '('}
        st = []

        for c in s:

            if c not in closeToOpen:
                st.append(c)

            else:
                if st:
                    top = st.pop()
                
                    if closeToOpen[c] != top:
                        return False
                
                else:
                    return False

        return not st
                
            




        