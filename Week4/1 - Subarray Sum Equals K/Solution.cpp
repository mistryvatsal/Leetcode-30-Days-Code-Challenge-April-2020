/*
 * Created on Thu Apr 23 2020
 *
 * Title: Leetcode - Subarray Sum Equals K
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int subarraySum(vector<int> &nums, int k) {
        int N=(int)nums.size();
        int count=0;
        int curr_sum=0;
        //Space : O(N)
        unordered_map<int, int> umap;
        //(0:1) pair. If there is a single element in array = k then single element subarray
        //is valid. hence req = curr_sum-k = 0, in this case this pair will be hit in umap.
        umap[0] = 1;
        //Time : O(N)
        for(int i=0; i<N; ++i) {
            curr_sum += nums[i];
            int req=curr_sum-k;
            count += umap[req];
            umap[curr_sum] += 1;
        }
        return count;
    }

    int subarraySum_Order_N(vector<int> &nums, int k) {
        int left = -1, right = -1, count = 0;
        int curr_sum = 0;
        
        int N = (int)nums.size();
        while (left < N && right < N && left <= right) {
            if(curr_sum < k) {
                right += 1;
                curr_sum += nums[right];
            }
            else if(curr_sum > k){
                left += 1;
                curr_sum -= nums[left];
            }
            else {
                count += 1;
                right += 1;
                curr_sum += nums[right];
            }
        }
        return count; 
    }
};

//Sample input case
int main()
{
    Solution obj;
    vector<int> v = {1, 1, 1};
    cout << obj.subarraySum_Order_N(v, 2) << endl;
    return 0;
}