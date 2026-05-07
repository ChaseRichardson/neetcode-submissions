class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        std::map<int, int> m;
        // store entries <number, index>
        m[nums[0]] = 0;

        for (int i = 1; i < nums.size(); ++i) {
            // if map has an entry 
            if (m.find(target - nums[i]) != m.end()) {
                return {m[target - nums[i]], i};
            }
            else {
                
                m[nums[i]] = i;
            }
        }
        return {};
    }
};
