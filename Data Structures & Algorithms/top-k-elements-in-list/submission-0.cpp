class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::map<int, int> m;
        std::vector<int> ret;
        std::vector<vector<int>> s(nums.size() + 1);
        
        // count elements in a map <num, count>
        for (int i = 0; i < nums.size(); ++i) {
            m[nums[i]] += 1;
        }

        for (const auto& items : m) {
            s[items.second].push_back(items.first);
        }

        // e is a vector in s
        for (int i = s.size() - 1; i > 0; --i) {
            for(int j = 0; j < s[i].size(); ++j) {
                if (ret.size() < k) {
                    ret.push_back(s[i][j]);
                }
            }
        }
        return ret;
    }
};
