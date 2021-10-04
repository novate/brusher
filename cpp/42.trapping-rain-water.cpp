#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int trap(vector<int> &height) {
    // the height of the water is max(0, min(l_max, r_max) - h_i)
    int l_ptr = 0, r_ptr = height.size() - 1;
    int l_max = 0, r_max = 0;
    int ans = 0;
    while (l_ptr <= r_ptr) {
      if (l_max <= r_max) {
        int h_water = max(0, min(l_max, r_max) - height[l_ptr]);
        l_max = max(l_max, height[l_ptr]);
        ans += h_water;
        l_ptr++;
      } else {
        int h_water = max(0, min(l_max, r_max) - height[r_ptr]);
        r_max = max(r_max, height[r_ptr]);
        ans += h_water;
        r_ptr--;
      }
    }
    return ans;
  }
};