/*
 * Created on Tue Apr 21 2020
 *
 * Title: Leetcode: Construct Binary Search Tree from Preorder
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        if(preorder.empty()) {
            return 0;
        }
        int root_value = preorder[0];
        TreeNode* root = new TreeNode(root_value);
        vector<int> smaller, greater;
        
        for(int i=0; i<(int)preorder.size(); ++i) {
            if(preorder[i] < root_value) {
                smaller.push_back(preorder[i]);
            }
            else {
                greater.push_back(preorder[i]);
            }
        }

        root->left = bstFromPreorder(smaller);
        root->right = bstFromPreorder(greater);

        return root;
    }
};