/*
 * Created on Fri Apr 10 2020
 *
 * Title: Leetcode - Counting Elements
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
    int countElements(vector<int>& arr) {
        unordered_map<int, int> umap;
        for(int i=0; i < arr.size(); i++) {
            umap[arr[i]]++;
        }
        int count = 0;
        for(int i=0; i < arr.size(); i++) {
            if(umap[arr[i] + 1] > 0) {
                count++;
            }
        }
        return count;
    }
};