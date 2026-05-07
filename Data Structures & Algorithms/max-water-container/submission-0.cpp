class Solution {
public:
    int maxArea(vector<int>& heights) {
        int retMax = 0;
        int l = 0;
        int r = heights.size() - 1;


        while (l < r) {
            int volume = min(heights[l], heights[r]) * (r - l);
            retMax = max(volume, retMax);

            if (heights[l] > heights[r]) {
                r -= 1;
            }
            else if (heights[l] < heights[r]) {
                l += 1;
            }
            else {
                l += 1;
            }
        }
        return retMax;
    }
};
