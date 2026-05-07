class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // set of all unique vals in nums
        std::unordered_set<int> s(nums.begin(), nums.end());
        int ret = 0;

        for (const auto &item : s) {
            // start of a new streak
            if (s.find(item - 1) == s.end()) {
                int length = 1;
                
                while(s.find(item + length) != s.end()) {
                    length += 1;
                }
                ret = max(ret, length);
            }   
        }
        return ret;
    }
};
