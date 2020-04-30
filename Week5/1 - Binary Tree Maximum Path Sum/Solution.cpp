/*
 * Created on Thu Apr 30 2020
 *
 * Title: Leetcode - Binary Tree Maximum Path Sum
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node as given below.
 * 
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int max_path_sum = 0;
    int dfs(TreeNode* root) {
        if(root == NULL) {
            return 0;
        }
        int left_sum = dfs(root->left);
        int right_sum = dfs(root->right);
        max_path_sum = max(max_path_sum, (root->val + left_sum + right_sum));
        return max(0, (root->val + max(left_sum, right_sum)));
    }

    int maxPathSum(TreeNode* root) {
        max_path_sum = INT32_MIN;
        dfs(root);
        return max_path_sum;
    }
};