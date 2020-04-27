/*
 * Created on Mon Apr 27 2020
 *
 * Title: Leetcode - Longest Common Subsequence
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    // Recursive function that calls itself
    // This approach will take O(2^n) time complexity, due to overlapping subproblems
    // This will take O(1) space complexity
    int LCS_Recursive(string &string1, string &string2, int i, int j) {
        if(string1[i] == '\0' || string2[j] == '\0') {
            return 0;
        }
        else if(string1[i] == string2[j]) {
            return 1 + LCS_Recursive(string1, string2, i+1, j+1);
        }
        else {
            return max(LCS_Recursive(string1, string2, i+1, j), LCS_Recursive(string1, string2, i, j+1));
        }
    }

    // Dynamic Programming approach
    // Time complexity will be O(m * n) where m and n are lengths of the input strings
    // Space complexity will be O(m * n) where m and n are lengths of the input strings
    int LCS_DP(string &text1, string &text2) {
        int m = text1.length() + 1;
        int n = text2.length() + 1;
        // Create a 2D array/vector and initialize it with 0
        vector<vector<int>> table(m, vector<int>(n, 0));
        for(int i=1; i<m; ++i) {
            for(int j=1; j<n; ++j) {
                if(text1[i-1] == text2[j-1]) {
                    table[i][j] = 1 + table[i-1][j-1];
                }
                else {
                    table[i][j] = max(table[i-1][j], table[i][j-1]);
                }
            }
        }
        // Last element will store the length of the longest common subsequence, 
        // hence return that
        return table[m-1][n-1];
    }
};

// Sample input cases
int main() {
    string text1 = "abc";
    string text2 = "abc";
    Solution obj;
    // Calling the recursive function
    cout << "Result using recursive : " << obj.LCS_Recursive(text1, text2, 0, 0);
    // Calling the DP function
    cout << "Result using dynamic programming : " << obj.LCS_DP(text1, text2) << endl;  
    return 0;
}