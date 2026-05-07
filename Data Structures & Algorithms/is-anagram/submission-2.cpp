class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> sCount(26, 0);
        vector<int> tCount(26, 0);

        for (int i = 0; i < s.length(); ++i) {
            int asciiS = s[i] - 97;
            int asciiT = t[i] - 97;
            sCount[asciiS] += 1;
            tCount[asciiT] += 1;
        }
        for (int i = 0; i < sCount.size(); ++i) {
            if (sCount[i] != tCount[i]) {
                return false;
            }
        }   
        return true;
    }
};
