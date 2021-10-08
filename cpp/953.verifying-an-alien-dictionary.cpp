#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  bool isAlienSorted(vector<string> &words, string order) {
    unordered_map<char, int> char_idx;
    for (int idx = 0; idx < order.length(); idx++) {
      char_idx[order[idx]] = idx;
    }
    for (int i = 0; i < words.size() - 1; i++) {
      for (int j = 0; j < words[i].size(); j++) {
        if (j >= words[i + 1].length()) {
          return false;
        }
        if (char_idx[words[i][j]] < char_idx[words[i + 1][j]]) {
          break;
        }
        if (char_idx[words[i][j]] > char_idx[words[i + 1][j]]) {
          return false;
        }
      }
    }
    return true;
  }
};