import java.util.HashMap;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        for (int idx = 0; idx < nums.length; idx++) {
            if (!hash.containsKey(nums[idx])) {
                hash.put(target - nums[idx], idx);
            }
            else {
                return new int[]{idx, hash.get(nums[idx])};
            }
        }
        // not found
        return new int[]{0, 0};
    }
}
// @lc code=end

