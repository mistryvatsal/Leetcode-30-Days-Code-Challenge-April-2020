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
        int left=0, right=0, count=0;
        int curr_sum=0;
        int N = nums.size();
        while (left < N && right < N) {
            if(curr_sum < k) {
                curr_sum += nums[right];
                right += 1;
            }
            else if(curr_sum > k){
                curr_sum -= nums[left];
                left += 1;
            }
            else {
                count++;
                curr_sum=0;
            }
        }
        if(curr_sum == k) {
                count += 1;
        }
        return count; 
    }
};

//Sample input case
int main()
{
    Solution obj;
    vector<int> v = {1, 2, 3};
    cout << obj.subarraySum_Order_N(v, 3) << endl;
    return 0;
}