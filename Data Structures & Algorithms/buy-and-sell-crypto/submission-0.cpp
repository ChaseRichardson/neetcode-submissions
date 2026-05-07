class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ret = 0;
        int l = 0;
        int r = 1;

        while (r < prices.size()) {
            if (prices[l] > prices[r]) {
                r += 1;
                l = r - 1;
            }
            else {
                ret = max(ret, prices[r] - prices[l]);
                r += 1;
            }  
        }
        return ret;
    }
};
