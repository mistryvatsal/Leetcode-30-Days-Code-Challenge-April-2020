/*
 * Created on Sun Apr 19 2020
 *
 * Title: Leetcode - Search in Rotated Sorted Array
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        // function to find the pivot.
        int findPivot(vector<int> &nums, int low, int high) {
            // Base cases
            if(high < low) return -1;
            if(low == high) return low;
            
            int mid = (low+high)/2;
            
            if(mid < high && nums[mid] > nums[mid+1]) {
                return mid;
            }
            else if(mid > low && nums[mid] < nums[mid-1]) {
                return mid -1;
            }
            else if(nums[low] >= nums[mid]) {
                return findPivot(nums, low, mid-1);
            }
            else {
                return findPivot(nums, mid+1, high);
            }            
        }
        // Implementation of Binary Search
        int binarySearch(vector<int> &nums, int low, int high, int target) {
            if (high>=low) {
                
                int mid = low + (high-low) / 2;
                
                if(target == nums[mid]) {
                    return mid;
                }
                
                if(nums[mid] > target) {
                    return binarySearch(nums, low, mid-1, target);
                }

                return binarySearch(nums, mid+1, high, target);
            }
            return -1;            
        }
        // Actual Search function.
        int search(vector<int> &nums, int target) {
            // If the array of numbers is empty return -1.
            if(nums.size() == 0) {
                return -1;
            }

            int low = 0;
            int high = nums.size()-1;
            // Calculate pivot.
            int pivot = findPivot(nums, low, high);
            // If pivot == -1, indicates the array is not rotated and hence, apply binary search on whole array.
            if(pivot == -1) {
                return binarySearch(nums, low, high, target);
            }
            // Check if target exists at pivot.
            if(nums[pivot] == target) {
                return pivot;
            }
            // Split the array into 2 parts and apply binar search over them.
            if(nums[0] <= target) {
                return binarySearch(nums, low, pivot-1, target);
            }
            else {
                return binarySearch(nums, pivot+1, high, target);
            }
        }
};

int main() {
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin) ;
    // freopen("output.txt", "w", stdout) ;
    // #endif
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL) ; cout.tie(NULL) ;

    //Sample Input.
    vector<int> nums = {1,3};
    int target = 0;
    Solution obj;
    cout << obj.search(nums, target);
}
