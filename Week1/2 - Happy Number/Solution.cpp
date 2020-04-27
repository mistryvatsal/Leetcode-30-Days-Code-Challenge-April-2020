/*
 * Created on Mon Apr 27 2020
 *
 * Title: Leetcode - Happy Number
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <unordered_set>
#include <cmath>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;
        while(n != 1) {
            int sum = 0;
            int curr = n;
            while(curr != 0) {
                sum += (int)pow((curr % 10), 2);
                curr /= 10;
            }
    
            if(seen.find(sum) != seen.end()) {
                return false;
            }
            seen.insert(sum);
            n = sum;
        }
        return true;
    }
};

int main() {
    int n = 20;
    Solution obj;
    cout << obj.isHappy(n) << endl;
    return 0;
}