/*
 * Created on Thu Apr 16 2020
 *
 * Title: Leetcode - Product of Array Except Self
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

// Time Complexity : O(n)
// Space Complexity : O(n)

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        // Object for returning the output. Doesn't count in space complexity.
        vector<int> outputArray(n);
        int R = 1;
        
        outputArray[0] = 1;
        for(int i=1; i<n; ++i) {
            outputArray[i] = outputArray[i-1] * nums[i-1];
        }

        for(int i=n-1; i>=0; i--) {
            outputArray[i] = outputArray[i] * R;
            R = R * nums[i];
        } 
        
        return outputArray;
    }
};

// Driver code with sample input.

int main() {
    Solution s;
    vector<int> i = {1, 2, 3, 4};
    vector<int> v;
    v = s.productExceptSelf(i);
    for(auto i : v) {
        cout << i << endl;
    }
    return 0;
}