/*
 * Created on Mon Apr 13 2020
 *
 * Title: Leetcode - Contiguous Array
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> counts;
        counts[0] = -1;
        int maxLength = 0, count = 0;
        for(int i=0; i < nums.size(); i++) {
            count = nums[i] == 0 ? count - 1 : count + 1;   
            if(counts.count(count)) {
                maxLength = max(maxLength, i - counts[count]);
            }
            else {
                counts.insert({ count, i });
            }
        }
        return maxLength;
    }
};