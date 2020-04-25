/*
 * Created on Sat Apr 25 2020
 *
 * Title: Leetcode - Jump Game
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

// Approach will be traversing the array from 0 to N-1 , maintaining a max_index variable
// holding the best/max value at index i

#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        // calculate N as the size of the array of numbers
        int N = nums.size();
        // take max_index to store the max position reached from index i
        // initially max_index equals first element
        int max_index = nums[0];
        for(int i=1; i<N; i++) {
            // if current_index (i) + element_at_current_index (nums[i]) is greater 
            // than max_index, this indicates, its the new max_index, hence
            // assign max_index with new value
            if((i + nums[i]) > max_index) {
                max_index = nums[i] + i;
            }
            // if at any point max_index eqauls current_index (i), it indicates
            // there is no move left further, hence break loop
            if(max_index == i) {
                break;
            }
        }
        // compare if max_index has reached last position or beyond last position
        // 
        // if(max_index >= N-1) {
        //     return true;
        // }
        // else {
        //     return false;
        // }
        // the below return statement is equivalent to above snippet
        return (max_index >= N-1);    
    }
};

// Sample Input cases
int main() {
    vector<int> input1 = {2,3,1,1,4};
    vector<int> input2 = {3,2,1,0,4};
    Solution obj;
    cout << obj.canJump(input1) << endl;
    cout << obj.canJump(input2) << endl; 
    return 0;
}