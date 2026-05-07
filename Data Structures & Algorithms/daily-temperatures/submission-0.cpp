class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<std::pair<int, int>> s;
        std::vector<int> v(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); ++i) {
            int t = (temperatures[i]);

            // pair is in forrm <temperature, indx>
            while(!s.empty() && t > s.top().first) {
                auto pair = s.top();
                s.pop();
                v[pair.second] = i - pair.second;
            }
            s.push({t, i});
        }

        return v;
    }
};
