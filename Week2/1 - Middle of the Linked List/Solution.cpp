/*
 * Created on Fri Apr 10 2020
 *
 * Title: Leetcode - Middle of the Linked List
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
    struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
      };
    
    public:
        ListNode* middleNode(ListNode* head) {
            if(head == NULL){
                return NULL;
            }
            
            ListNode *curr;
            curr = head;
            int count = 0;
            
            unordered_map<int, ListNode*> umap;
            while(curr != NULL) {
                umap[count] = curr; 
                curr = curr->next;
                count++;
            }
            
            int mid = count / 2;
            return umap[mid];
        }
};