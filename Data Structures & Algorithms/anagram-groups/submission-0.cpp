class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::vector<int>, std::vector<std::string>> m;
        for (int i = 0; i < strs.size(); ++i) {
            std::vector<int> signature(26, 0);
            for (auto &c : strs[i]) {
                int cNum = toascii(c) - 97;
                signature[cNum] += 1;
            }
            m[signature].push_back(strs[i]);
        }      
        std::vector<std::vector<std::string>> ret;
        for (auto &p : m) {
            ret.push_back(p.second);
        }
        return ret;
    }
};
