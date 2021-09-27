#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> hash;
    for (int idx = 0; idx < nums.size(); idx++) {
      auto it = hash.find(nums[idx]);
      if (it != hash.end()) {
        return {idx, hash[nums[idx]]};
      } else {
        hash[target - nums[idx]] = idx;
      }
    }
    // not found, return undefined
    return {0, 0};
  }
};