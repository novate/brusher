#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>> &intervals) {
    sort(intervals.begin(), intervals.end(),
         [](const vector<int> &a, const vector<int> &b) -> bool {
           return a[0] < b[0];
         });
    vector<vector<int>> ans;
    int cur_begin = intervals[0][0];
    int cur_end = intervals[0][1];
    for (auto interval : intervals) {
      if (interval[0] <= cur_end) {
        cur_end = max(cur_end, interval[1]);
      } else {
        ans.push_back({cur_begin, cur_end});
        cur_begin = interval[0];
        cur_end = interval[1];
      }
    }
    ans.push_back({cur_begin, cur_end});
    return ans;
  }
};