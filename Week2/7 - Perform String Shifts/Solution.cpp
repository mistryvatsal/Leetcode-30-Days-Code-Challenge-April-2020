/*
 * Created on Wed Apr 15 2020
 *
 * Title: Leetcode - Perform String Shifts
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int totalAmount = 0;
        for(vector<int> p : shift) {
            if(p[0] == 0) {
                totalAmount -= p[1];
            }
            else {
                totalAmount += p[1];
            }
        }
        int n = s.length();
        totalAmount = totalAmount % n;
        if(totalAmount < 0) {
            totalAmount += n;
        }
        return s.substr(n-totalAmount) + s.substr(0, n-totalAmount);
    }
};