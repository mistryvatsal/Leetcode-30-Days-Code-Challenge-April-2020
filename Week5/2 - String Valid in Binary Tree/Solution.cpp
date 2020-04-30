/*
 * Created on Thu Apr 30 2020
 *
 * Title: Leetcode - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>

using namespace std;

// Definition for a binary tree node. 
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
    bool valid_path_using_dfs(TreeNode* root, vector<int>& arr, int idx) {
        if(root->val != arr[idx]) return false;

        if(idx == arr.size()-1) return !root->left && !root->right;
        
        return ((root->left && valid_path_using_dfs(root->left, arr, idx+1)) || (root->right && valid_path_using_dfs(root->right, arr, idx+1))); 
    }
    bool isValidSequence(TreeNode* root, vector<int>& arr) {
        if(!root) return arr.size() == 0;
        
        return valid_path_using_dfs(root, arr, 0);
    }
};