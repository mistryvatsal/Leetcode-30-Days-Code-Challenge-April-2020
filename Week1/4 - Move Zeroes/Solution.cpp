/*
 * Created on Fri Apr 10 2020
 *
 * Title: Leetcode - Move Zeroes
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++) {
            for(int j=0; j<nums.size() - 1; j++) {
                if(nums[j] == 0 && nums[j+1] != 0) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                }
            }
        }
    }
};