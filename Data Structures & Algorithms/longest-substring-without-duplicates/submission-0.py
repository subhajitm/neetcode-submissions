class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        st = set()
        l, r = 0, 0
        for r in range(len(s)):
            if s[r] not in st:
                st.add(s[r])
            else:
                while s[r] in st:
                    st.remove(s[l])
                    l += 1
                st.add(s[r])
            res = max(res, r - l + 1)

        return res