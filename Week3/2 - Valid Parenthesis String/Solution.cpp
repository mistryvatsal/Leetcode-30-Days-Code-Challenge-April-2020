/*
 * Created on Thu Apr 16 2020
 *
 * Title: Leetcode - Valid Parenthesis String
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
        int n = s.size();

        if(n == 0) {
            return true;
        }    
        stack<int> main_stack, star_stack;

        for(int i=0; i<n; ++i) {
            if(s[i] == '(') {
                main_stack.push(i);
            }
            else if(s[i] == '*') {
                star_stack.push(i);
            }
            else {
                if(!main_stack.empty()) {
                    main_stack.pop();
                }
                else if(!star_stack.empty()) {
                    star_stack.pop();
                }
                else {
                    return false;
                }
            }
        }

        while(!main_stack.empty()) {
            if(star_stack.empty()) {
                return false;
            }
            else if(main_stack.top() < star_stack.top()) {
                main_stack.pop();
                star_stack.pop();
            }
            else {
                return false;
            }
        }
        return true;    
    }
};